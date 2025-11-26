# 🎓 Student Performance Dashboard

A **Streamlit-based web dashboard** that visualizes and analyzes student academic performance.  
It helps educators, administrators, and data teams monitor **scores, attendance, and performance trends** interactively.

---

## 📊 Project Overview
This dashboard is built using **Python, Streamlit, Pandas, Matplotlib, and Seaborn**.  
It loads cleaned student data from a CSV file, performs filtering by subject, performance category, and date range, and displays **real-time insights** through dynamic charts and metrics.

---

## 🚀 Features

### 🎛️ Sidebar Filters
- Select specific **subjects** or view all.
- Filter by **performance category** (High / Medium / Low).
- Choose a **custom date range** for time-based analysis.
- Displays **page load time** with visual indicators (✅ or ⚠️).

### 📈 Key Metrics
Displayed at the top of the dashboard:
- **Total Records**  
- **Average Score**  
- **Attendance Rate (%)**  
- **High Performers Count**

### 📊 Visualizations
1. **Average Score Trends by Subject**  
   - Line chart showing monthly average scores across subjects.  
   - Automatically adjusts x-axis ticks for readability.

2. **Attendance Rate Heatmap**  
   - Heatmap visualizing attendance rates by subject and month.  
   - Blue intensity represents attendance percentage.

3. **Performance Distribution by Subject**  
   - Countplot showing how performance levels vary across subjects.

4. **Top 10 High Performers (Score ≥ 95)**  
   - Table highlighting top-scoring students with their subjects and attendance status.

5. **Attendance vs Performance Category**  
   - Bar chart comparing attendance status with performance levels.

---

## 🧠 Data Preparation

The dashboard expects a **cleaned CSV file** named:
```

work ready data/cleaned_data.csv

````

### Required Columns
| Column Name | Description |
|--------------|-------------|
| `student_id` | Unique student identifier |
| `name` | Student’s full name |
| `subject` | Subject name (e.g., Math, Biology) |
| `score` | Student’s score (numeric) |
| `date` | Exam or attendance date |
| `attendance` | “Present” or “Absent” |
| `categorize_performance` | “High”, “Medium”, or “Low” |

🧹 *Unknown or invalid values are cleaned automatically during loading.*

---

## ⚙️ How It Works

### 1. Load & Clean Data
```python
@st.cache_data(ttl=3600)
def load_and_clean_data():
    df = pd.read_csv("work ready data/cleaned_data.csv")
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['score'] = df['score'].round(1)
    df['attendance'] = df['attendance'].str.capitalize()
    df['categorize_performance'] = df['categorize_performance'].str.capitalize()
    df['year_month'] = df['date'].dt.to_period('M')
    df['month'] = df['date'].dt.month
    return df
````

* Cached for **1 hour** to improve load performance.
* Cleans attendance and performance labels.
* Converts dates and extracts monthly periods.

### 2. User Filters

The sidebar allows interactive filtering by:

* Subject
* Performance category
* Date range

### 3. Visual Rendering

Charts are dynamically updated based on filters using **Matplotlib** and **Seaborn**.

---

## 🖥️ Running the App

### Prerequisites

Make sure you have:

* **Python 3.9+**
* The following Python packages:

  ```bash
  pip install streamlit pandas matplotlib seaborn
  ```

### Run Command

```bash
streamlit run app.py
```

Then open the local link (usually [http://localhost:8501](http://localhost:8501)) to view the dashboard.

oooooor

we hosted the dashboard for you to easily view it from [this link](https://student-performance-dashboard-qhcvej2b585q9xpepcfmzb.streamlit.app/)

---

## 🧩 File Structure

```
📁 Student-Performance-Dashboard
├── app.py                         # Streamlit dashboard code
├── work ready data/
│   └── cleaned_data.csv           # Cleaned input dataset
├── visualization/
│   └──visuals_notebook.ipynb      # Visualization notebook
│   └──readme.md          # Notebook documentation
│   └──streamlit_readme.md         #streamlit documentation
├── README.md                      # Project documentation
└── requirements.txt               # Dependencies list
```

---

## ⏱️ Performance Notes

* Data loading time is displayed in the sidebar.
* If the page load exceeds **3 seconds**, a warning appears.
* Caching reduces reload delays between filter changes.

---

## 📸 Example Outputs

| Visualization             | Description                                         |
| ------------------------- | --------------------------------------------------- |
| **Score Trends**          | Shows average student scores over time per subject. |
| **Heatmap**               | Displays attendance rate by month and subject.      |
| **Performance Bar Chart** | Compares student performance levels.                |
| **Top Performers Table**  | Highlights the highest-scoring students.            |

---