# 🗃️ Milestone 2: SQL Integration & Querying

This milestone focuses on **designing a normalized relational database**, **importing cleaned student data**, and **writing analytical SQL queries** to extract meaningful insights.

## 🎯 Objectives
- Store preprocessed student data in a structured MySQL database  
- Apply database normalization principles  
- Enable efficient querying for performance and attendance trends  

## 📂 Files Included

| File | Description |
|------|-------------|
| `school_management_depi_raw_data.sql` | Script to create and populate a temporary `raw_data` table |
| `school_management_depi_students.sql` | Creates the normalized `students` table |
| `school_management_depi_performance.sql` | Creates the `performance` table with foreign key to `students` |
| `schema_diagram.png` | ER diagram of the final database schema *(to be added)* |

> 💡 The `date` column was intentionally **excluded** from the final schema, as it was determined to add limited value for the required queries.

## 🏗️ Database Schema

### Tables Created

#### 1. `students`
- `student_id` (PK)  
- `name`  
- `subject`

> Stores unique student-subject combinations.

#### 2. `performance`
- `performance_id` (PK, auto-increment)  
- `student_id` (FK → `students.student_id`)  
- `score`  
- `attendance`  
- `categorize_performance`

> Stores measurable academic records linked to students.

### Normalization Approach
- Eliminated redundancy by splitting entity (`students`) from measurements (`performance`)
- Ensured referential integrity via foreign key constraint

## 🧪 Sample Queries Implemented

The SQL scripts include:
- Insertion of unique students from raw data  
- Population of performance records  
- Validation queries:
  ```sql
  SELECT COUNT(*) AS total_students FROM students;
  SELECT COUNT(*) AS total_performance_records FROM performance;
  SELECT * FROM students LIMIT 10;
  SELECT * FROM performance LIMIT 10;
  ```

These support the required analytical tasks:
- Top performers by subject  
- Attendance trends  
- Average scores by time period (handled later in Python due to `date` removal)

## 📤 Deliverables

- Normalized **ER diagram** (`schema_diagram.png`)  
- **SQL scripts** for schema creation and data import  
- **Query results** (screenshots or exported data — to be added in final report)

## 🔗 Next Steps
- The database structure informs data expectations in **[Milestone 3](../milestone3_visualization/streamlit_readme.md)**  
- Although the dashboard uses the `cleaned_data.csv` directly (for time-based analysis), the SQL work demonstrates core database management skills per project requirements

> ✅ This milestone fulfills the **SQL & Database Management** module objectives through practical implementation.
