# 🎓 Student Performance Dashboard  
**Final Project – DEPI: AI & Data Science | Data engineering Track (Round 3)**  
*Modules: Programming Essentials + SQL & Database Management*

---

## 🎯 Project Overview

This project builds an end-to-end **Student Performance Dashboard** that collects, stores, analyzes, and visualizes academic data to help educators monitor student progress.  

It demonstrates a complete data pipeline:  
**Raw CSVs → Cleaned Dataset → Normalized Database → Visual Insights → Interactive Dashboard**

By the end, we deliver a functional system that answers key questions like:
- Who are the top performers in each subject?
- How does attendance affect academic performance?
- What are the monthly trends in student scores?

---

## 👥 Team Members & Contributions

| Member   | Milestone | Responsibility |
|--------|----------|----------------|
| **Maram**     | 1 | Merged raw CSVs, handled duplicates & nulls, cleaned data |
| **Marawan & Linah** | 2 | Designed MySQL schema, implemented normalized tables, wrote SQL queries |
| **Khaled**    | 3 | Built visualizations (notebook) and interactive Streamlit dashboard |

---

## 📁 Repository Structure

```
student-performance-dashboard/
├── data/
│   ├── raw/               # Original CSV files (students, courses, attendance, grades)
│   └── processed/         # Cleaned datasets (raw_students.csv, cleaned_data.csv)
│
├── src/
│   ├── milestone1_preprocessing/  # Data merging & cleaning (Maram)
│   ├── milestone2_sql/           # Database schema & SQL scripts (Marawan, Linah)
│   └── milestone3_visualization/ # Visualizations & Streamlit dashboard (Khaled)
│
├── docs/                  # Final report & presentation slides (Milestone 4)
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

---

## 🚀 How to Run the Project

### 1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 2. **Explore Each Milestone**

#### 🧹 Milestone 1 – Data Preprocessing
- Notebooks: `src/milestone1_preprocessing/data.ipynb`, `data_cleaning.ipynb`
- Output: `data/processed/cleaned_data.csv`

#### 🗃️ Milestone 2 – SQL & Database
- Run SQL scripts in your MySQL client:
  ```sql
  SOURCE src/milestone2_sql/school_management_depi_students.sql;
  SOURCE src/milestone2_sql/school_management_depi_performance.sql;
  ```
- View schema: `src/milestone2_sql/schema_diagram.png`

#### 📊 Milestone 3 – Visualization & Dashboard
- **Static analysis**: Open `src/milestone3_visualization/visuals_notebook.ipynb`
- **Interactive dashboard**:
  ```bash
  streamlit run src/milestone3_visualization/dashboard/app.py
  ```
- **Live hosted version**:  
  🔗 [https://student-performance-dashboard-qhcvej2b585q9xpepcfmzb.streamlit.app/](https://student-performance-dashboard-qhcvej2b585q9xpepcfmzb.streamlit.app/)

---

## 📦 Key Files

| File | Purpose |
|------|--------|
| `data/processed/cleaned_data.csv` | Final clean dataset (used by Milestones 2 & 3) |
| `src/milestone2_sql/*.sql` | Database creation and data import scripts |
| `src/milestone3_visualization/dashboard/app.py` | Main Streamlit dashboard |
| `docs/final_report.pdf` | Final documentation (in progress) |
| `docs/presentation_slides.pdf` | Presentation slides (in progress) |

---

## 📝 Milestone Deliverables Summary

| Milestone | Deliverables |
|---------|--------------|
| **1. Data Preprocessing** | Python notebooks, cleaned CSV |
| **2. SQL Integration** | Normalized schema, ER diagram, SQL scripts, query results |
| **3. Visualization** | Jupyter notebook, Streamlit dashboard |
| **4. Final Report** | PDF report + presentation slides *(to be submitted)* |

---

## 🌟 Highlights

- ✅ Realistic data pipeline with intentional messiness (duplicates, nulls)  
- ✅ Proper database normalization (students ↔ performance)  
- ✅ Rich visual insights: score trends, attendance heatmaps, performance distribution  
- ✅ Fully interactive, filterable dashboard with live metrics  
- ✅ Hosted and publicly accessible via Streamlit Cloud  

---

✨ *Submitted as part of the DEPI: AI & Data Science | Data engineering Track – Round 3 Final Project*  