# 🎓 Student Performance Data Visualization Notebook

This notebook explores and visualizes student academic performance and attendance trends using the cleaned dataset from Milestone 1. It fulfills the **Visualization & Reporting** requirements of the Student Performance Dashboard project.

## 🧩 Overview

The goal of this notebook is to:
- Explore performance across subjects
- Identify trends in scores and attendance over time
- Generate visual insights for educators and administrators

All analysis is performed in Python using **pandas**, **matplotlib**, and **seaborn**.

## 📘 Notebook Structure

### 1️⃣ Importing Libraries & Loading Data
- Loads `cleaned_data.csv` from `data/processed/`
- Applies final cleaning:
  - Converts `date` to datetime
  - Rounds scores to 1 decimal
  - Replaces `"Unknown"` attendance with `"Absent"`
  - Removes rows with `"Unknown"` in `name` or `subject`
  - Standardizes capitalization

### 2️⃣ Date & Time Feature Extraction
New columns added:
- `year`
- `month`
- `year_month` (e.g., `2023-09`) → used for monthly grouping

### 3️⃣ Average Score Trends by Subject
- Groups by `subject` and `year_month`
- Applies 3-month rolling average
- Plots line chart per subject  
✅ *Reveals seasonal patterns and subject progress*

### 4️⃣ Attendance vs Performance Category
- Countplot comparing `"Present"` vs `"Absent"` across `"High"`, `"Medium"`, `"Low"`  
✅ *Shows correlation between attendance and performance*

### 5️⃣ Attendance Rate Heatmap
- Converts attendance to numeric (1 = Present, 0 = Absent)
- Creates pivot table: **subject × month**
- Visualizes attendance % as a heatmap  
✅ *Highlights low-engagement months or subjects*

### 6️⃣ Performance Distribution Across Subjects
- Countplot of performance categories per subject  
✅ *Identifies subjects where students struggle or excel*

### 7️⃣ Data Preview
- Displays first 50 rows to validate:
  - Date formatting
  - Cleaned "Unknown" values
  - Consistent capitalization

## 📊 Summary of Insights
- Attendance strongly correlates with high performance
- Score trends reveal steady improvement in core subjects
- Certain months show dips in attendance (e.g., exam periods)
- Visualization outputs feed directly into the Streamlit dashboard

## 🧠 Tools Used
| Category         | Libraries                |
|------------------|--------------------------|
| Data Processing  | `pandas`                 |
| Visualization    | `matplotlib`, `seaborn`  |
| Environment      | Jupyter Notebook         |
| Data Format      | CSV (`cleaned_data.csv`) |
