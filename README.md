# 🎓 Student Performance Dashboard – Full Project Documentation

## 📌 Overview

This project demonstrates an end-to-end data pipeline for cleaning and visualizing student performance data using modern open-source tools:

- **Raw data**: CSV file with student records  
- **Transformation**: `dbt` (data build tool) with DuckDB  
- **Orchestration**: Apache Airflow (Docker-based)  
- **Visualization**: Streamlit dashboard  
- **Persistence**: Single `.duckdb` file shared across components

The goal is to produce a clean, analysis-ready dataset and expose it via an interactive dashboard — all reproducible and containerized.

---

## 🗂️ 1. Project Structure

```text
Student-performance-dashboard/
├── docker-compose.yaml          # Airflow + services
├── requirements.txt             # Python dependencies (dbt, duckdb, etc.)
├── dags/
│   └── dbt_student_pipeline.py  # Airflow DAG
├── include/
│   └── dbt/                     # dbt project root
│       ├── dbt_project.yml
│       ├── profiles.yml
│       ├── seeds/
│       │   └── raw_students.csv
│       └── models/
│           └── cleaned_students.sql
├── data/                        # Shared volume
│   └── student_performance.duckdb  # Output database
└── streamlit_app/
    └── app.py                   # Streamlit dashboard
```

---

## 🧹 2. Data Cleaning with dbt + DuckDB

### Input
`seeds/raw_students.csv` contains:
```csv
student_id,name,subject,score,date,attendance
1,Ali,Math,85,2024-09-01,
2,Fatima,Science,92,2024-09-01,Present
...
```

### Transformation Logic (`models/cleaned_students.sql`)
```sql
{{ config(materialized='table') }}

SELECT
    student_id,
    name,
    subject,
    score,
    date,
    CASE
        WHEN attendance IS NULL OR TRIM(attendance) = '' THEN 'Absent'
        ELSE attendance
    END AS attendance
FROM {{ ref('raw_students') }}
WHERE
    student_id IS NOT NULL AND TRIM(CAST(student_id AS VARCHAR)) != ''
    AND name IS NOT NULL AND TRIM(name) != ''
    AND subject IS NOT NULL AND TRIM(subject) != ''
    AND score IS NOT NULL AND TRIM(CAST(score AS VARCHAR)) != ''
    AND date IS NOT NULL AND TRIM(date) != ''
```

**Rules applied**:
- Replace empty/NULL `attendance` with `"Absent"`
- Drop any row with missing values in other columns
- Output stored as a **persistent table** in DuckDB

### dbt Configuration

- **Project name**: `student_performance`
- **Adapter**: `duckdb`
- **Output path**: `/opt/airflow/data/student_performance.duckdb` (mounted volume)

---

## 🛠️ 3. Orchestration with Apache Airflow

### DAG: `dags/dbt_student_pipeline.py`
```python
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

DBT_PROJECT_DIR = "/opt/airflow/include/dbt"
DBT_PROFILES_DIR = "/opt/airflow/include/dbt"

with DAG(
    "dbt_student_performance",
    start_date=datetime(2025, 11, 30),
    schedule="@daily",
    catchup=False,
) as dag:

    dbt_seed = BashOperator(
        task_id="dbt_seed",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt seed",
        env={"DBT_PROFILES_DIR": DBT_PROFILES_DIR},
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt run",
        env={"DBT_PROFILES_DIR": DBT_PROFILES_DIR},
    )

    dbt_seed >> dbt_run
```

### Key Features
- Runs daily (or manually via UI)
- Uses `BashOperator` to call `dbt seed` → `dbt run`
- All paths are container-relative and volume-mounted
- Outputs written to shared `data/` folder

### Docker Setup
- Airflow runs via `docker-compose`
- Custom dependencies (`dbt-core`, `dbt-duckdb`) installed via `_PIP_ADDITIONAL_REQUIREMENTS` or custom image
- Volumes ensure:
  - DAGs and dbt code are accessible
  - `.duckdb` file persists across runs

---

## 📊 4. [Streamlit Dashboard](https://khaled-0110-student-performance-dashboard-app-gtqepr.streamlit.app/)

### File: `streamlit_app/app.py`
```python
import streamlit as st
import duckdb

# Connect to shared DuckDB file
con = duckdb.connect('data/student_performance.duckdb')

# Load data
df = con.execute("SELECT * FROM cleaned_students").fetchdf()

# UI
st.title("🎓 Student Performance Dashboard")
st.dataframe(df)

# Example chart
st.subheader("Attendance Summary")
attendance_counts = df['attendance'].value_counts()
st.bar_chart(attendance_counts)
```

### Integration Notes
- Streamlit app runs in its own container (or locally)
- Mounts the same `data/` folder to access `student_performance.duckdb`
- No ETL needed — reads directly from DuckDB

---

## 🐳 5. Docker & Deployment

### Airflow `docker-compose.yaml` Highlights
```yaml
x-airflow-common:
  &airflow-common
  environment:
    _PIP_ADDITIONAL_REQUIREMENTS: "dbt-core dbt-duckdb"
  volumes:
    - ./dags:/opt/airflow/dags
    - ./include:/opt/airflow/include
    - .//opt/airflow/data

services:
  airflow-webserver:
    <<: *airflow-common
    command: webserver
    ports:
      - "8080:8080"
```

### Streamlit Docker (optional)
```Dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "streamlit_app/app.py", "--server.port=8501"]
```

With volume:
```yaml
volumes:
  - ./data:/app/data
```

---

## ✅ 6. Key Advantages

| Component | Benefit |
|--------|--------|
| **dbt** | Version-controlled, tested, and documented transformations |
| **DuckDB** | Zero-setup embedded analytics database; fast SQL on files |
| **Airflow** | Reliable scheduling, monitoring, and retries |
| **Streamlit** | Rapid dashboard development with minimal code |
| **Docker** | Full reproducibility across environments |

---

## 🔜 7. Next Steps & Improvements

- Add unit tests in dbt (`schema.yml` + `test` blocks)
- Parameterize date ranges in Streamlit
- Add error notifications in Airflow (Slack/email)
- Replace `_PIP_ADDITIONAL_REQUIREMENTS` with custom Docker image
- Deploy to cloud (e.g., AWS ECS, GCP Cloud Run)

---

## 📚 8. How to Run Locally

1. Clone the repo
2. Place `raw_students.csv` in `include/dbt/seeds/`
3. Run:
   ```bash
   export _PIP_ADDITIONAL_REQUIREMENTS="dbt-core dbt-duckdb"
   docker-compose up -d
   ```
4. Visit Airflow at `http://localhost:8080`, trigger DAG
5. Run Streamlit:
   ```bash
   streamlit run streamlit_app/app.py
   ```
