# 🧹 Milestone 1: Data Collection & Preprocessing

This milestone focuses on **collecting, merging, and cleaning raw student data** to prepare a reliable dataset for database ingestion and analysis.

## 📁 Input Files
Original CSV files (located in `data/raw/`):
- `students.csv` – Student names and IDs  
- `courses.csv` – Subject/course information  
- `attendance.csv` – Attendance records  
- `grades.csv` – Academic scores  

> ⚠️ No single complete dataset was available, so these files were combined to simulate real-world fragmented data.

## 🛠️ Workflow

### 1. **Data Merging**  
- Notebook: [`data.ipynb`](data.ipynb)  
- Merged all 4 CSVs into a single file: `raw_students.csv`  
- Intentionally introduced **duplicates and null values** to reflect messy real-world data

### 2. **Data Cleaning**  
- Notebook: [`data_cleaning.ipynb`](data_cleaning.ipynb)  
- Performed the following operations:
  - Removed duplicate records  
  - Handled missing (`null`) values  
  - Standardized column formats  
  - Categorized performance into: `"High"`, `"Medium"`, `"Low"` based on score thresholds  
- Output: **`cleaned_data.csv`** (saved to `data/processed/`)

## 📤 Deliverables

| File | Description |
|------|-------------|
| `data.ipynb` | Merges raw CSVs → creates `raw_students.csv` |
| `data_cleaning.ipynb` | Cleans `raw_students.csv` → produces `cleaned_data.csv` |
| `data/processed/cleaned_data.csv` | Final clean dataset used in Milestones 2–4 |

## 📊 Final Dataset Schema (`cleaned_data.csv`)

| Column | Description |
|--------|-------------|
| `student_id` | Unique student identifier |
| `name` | Student’s full name |
| `subject` | Academic subject (e.g., Math, Biology) |
| `score` | Numeric score (0–100) |
| `date` | Date of assessment or attendance record |
| `attendance` | `"Present"` or `"Absent"` |
| `categorize_performance` | `"High"` (≥85), `"Medium"` (60–84), `"Low"` (<60) |

> ✅ This cleaned dataset is the **single source of truth** for the rest of the project.

## 🔗 Next Steps
- The `cleaned_data.csv` file is imported into MySQL in **[Milestone 2](../milestone2_sql/readme.md)**  
- It also powers all visualizations in **[Milestone 3](../milestone3_visualization/streamlit_readme.md)**
