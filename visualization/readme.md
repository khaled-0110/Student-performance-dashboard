# 🎓 Student Performance Data Visualization Notebook

This notebook visualizes student performance and attendance trends based on the cleaned dataset prepared by the data preprocessing team.  
It represents the **Visualization & Dashboard** milestone of the *Student Performance Dashboard Project*.

---

## 🧩 Overview
The goal of this notebook is to:
- Explore and visualize academic performance across subjects.
- Identify patterns and trends in scores and attendance.
- Provide visual insights that can later be used in a dashboard or final presentation.

All analysis is performed in **Python** using `pandas`, `matplotlib`, and `seaborn`.

---

## 📘 Notebook Structure

### 1️⃣ Importing Libraries and Loading the Dataset
This section imports the required Python libraries for data manipulation and visualization:
- `pandas` for data handling and cleaning.
- `matplotlib.pyplot` and `seaborn` for creating visualizations.

The dataset (`cleaned_data.csv`) is loaded and cleaned by:
- Converting the `date` column to proper datetime format.
- Rounding all `score` values to one decimal place.
- Replacing `"Unknown"` values in `attendance` with `"Absent"`.
- Removing rows where `subject` or `name` was `"Unknown"`.
- Standardizing capitalization for consistency.

This ensures clean and uniform data for analysis.

---

### 2️⃣ Date and Time Feature Extraction
New time-based columns are added to facilitate trend analysis:
- `year` → Extracted from `date`.
- `month` → Extracted from `date`.
- `year_month` → Combines year and month (e.g., `2023-09`) for smoother monthly grouping.

These fields are later used to track how scores and attendance evolve over time.

---

### 3️⃣ Average Score Trends by Subject
This visualization examines how average student scores change across time for each subject.

**Process:**
- Group by `subject` and `year_month` to calculate the mean `score`.
- Apply a 3-month rolling average to smooth fluctuations.
- Plot line graphs for each subject with distinct colors.

**Insights:**
- Reveals seasonal or long-term patterns.
- Helps compare progress between different subjects.

Each subject’s trend line helps educators identify which subjects show steady improvement or decline.

---

### 4️⃣ Attendance vs Performance Category
This plot explores the relationship between **attendance** and **performance level** (High, Medium, Low).

A `countplot` compares the number of records for “Present” vs “Absent” students in each performance category.

**Purpose:**
- Identify if attendance impacts performance.
- Highlight how many top performers maintain consistent attendance.

---

### 5️⃣ Attendance Rate Heatmap
A heatmap visualizing attendance percentages across **subjects** and **months**.

**Steps:**
- Convert attendance values to numerical (1 for Present, 0 for Absent).
- Create a pivot table showing attendance rate per subject per month.
- Visualize with `seaborn.heatmap`.

**Insights:**
- Darker areas indicate higher attendance.
- Quickly reveals months or subjects with low participation or engagement.

---

### 6️⃣ Performance Distribution Across Subjects
This section compares how many students fall into each performance category (High, Medium, Low) across different subjects.

A `countplot` shows:
- Number of students per performance level.
- Variation in student achievement between subjects.

**Use Case:**
- Detect subjects where most students struggle.
- Identify where teaching methods might need adjustment.

---

### 7️⃣ Data Preview
Displays the first 50 rows of the cleaned dataset to verify:
- Correct formatting for `date`.
- No “Unknown” values remain.
- Properly capitalized and standardized fields.

This serves as a final validation step before using the data for dashboard development.

---

## 📊 Summary
Through the notebook, we:
- Cleaned and standardized the dataset.
- Visualized trends in performance and attendance.
- Gained insight into how student scores evolve over time.
- Identified the relationship between attendance and academic success.

These visual results form the foundation for the **final dashboard** and **project presentation** in the next milestone.

---

## 🧠 Tools Used
| Category | Libraries |
|-----------|------------|
| Data Processing | pandas |
| Visualization | matplotlib, seaborn |
| File Format | CSV |
| Notebook Environment | Jupyter Notebook |
