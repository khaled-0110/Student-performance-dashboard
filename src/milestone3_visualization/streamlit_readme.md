# 🎓 Student Performance Dashboard (Streamlit)

A dynamic web dashboard built with **Streamlit**, visualizing student academic performance, attendance trends, and score patterns.

## 🚀 Features

- **Interactive Filters**: Subject, Performance Category, Date Range  
- **Live Metrics**: Total Records, Avg Score, Attendance Rate, High Performers  
- **Visualizations**:
  - Average Score Trends by Subject (Line Chart)
  - Attendance Heatmap (by Month & Subject)
  - Performance Distribution by Subject (Bar Chart)
  - Top 10 High Performers Table (Score ≥ 95)
  - Attendance vs Performance Category (Bar Chart)

## 🧩 Data Requirements

The dashboard expects the cleaned dataset at:  
`../../data/processed/cleaned_data.csv` (relative to this `dashboard/` folder)

### Required Columns
| Column | Description |
|--------|-------------|
| `student_id` | Unique student identifier |
| `name` | Student’s full name |
| `subject` | Subject name (e.g., Math, Biology) |
| `score` | Numeric score (0–100) |
| `date` | Exam or attendance date (YYYY-MM-DD) |
| `attendance` | `"Present"` or `"Absent"` |
| `categorize_performance` | `"High"`, `"Medium"`, or `"Low"` |

> ⚠️ The app automatically standardizes and cleans minor inconsistencies (e.g., capitalization, "Unknown" values) during load.

## ⚙️ How to Run

### Prerequisites
Ensure you have Python 3.9+ and install dependencies:
```bash
pip install streamlit pandas matplotlib seaborn
```

### Run Locally
From the **repository root**, run:
```bash
streamlit run src/milestone3_visualization/dashboard/app.py
```

👉 **Live hosted version**:  
[https://student-performance-dashboard-qhcvej2b585q9xpepcfmzb.streamlit.app/](https://student-performance-dashboard-qhcvej2b585q9xpepcfmzb.streamlit.app/)

## 📁 File Structure

```
src/milestone3_visualization/
├── visuals_notebook.ipynb     # Static visualizations (Seaborn/Matplotlib)
├── README.md                  # This file
└── dashboard/
    ├── app.py                 # Main Streamlit application
    └── requirements.txt       # Optional: dashboard-specific deps
```

## ⏱️ Performance Notes

- Data is cached for 1 hour using `@st.cache_data(ttl=3600)` to improve responsiveness.
- Page load time is displayed in the sidebar.
- A ⚠️ warning appears if initial load exceeds 3 seconds.
- Filters update visualizations instantly without reloading the full dataset.
  