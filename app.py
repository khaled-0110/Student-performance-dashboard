import streamlit as st
import pandas as pd
import duckdb
import matplotlib.pyplot as plt
import seaborn as sns
import time
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# 🔧 CONFIG: Update these to match your setup
DUCKDB_PATH = "data/student_performance.duckdb"  # Relative to Streamlit working dir
TABLE_NAME = "cleaned_students"  # Must match your dbt model name

start_time = time.time()

@st.cache_data(ttl=3600)
def load_data():
    db_path = Path(DUCKDB_PATH)
    if not db_path.exists():
        st.error(f"DuckDB file not found at `{DUCKDB_PATH}`. Please run the Airflow DAG first.")
        return pd.DataFrame()

    try:
        con = duckdb.connect(str(db_path), read_only=True)
        df = con.execute(f"SELECT * FROM {TABLE_NAME}").fetchdf()
        con.close()
        return df
    except Exception as e:
        st.error(f"Failed to load data from DuckDB: {e}")
        return pd.DataFrame()

# Load data
data = load_data()

# Early exit if no data
if data.empty:
    st.stop()

# 🔧 DATA PREPARATION (adjust based on actual columns)
# Note: Your current dbt model does NOT have 'categorize_performance'
# So we create it here based on score
def categorize_score(score):
    if score >= 90:
        return "High"
    elif score >= 70:
        return "Medium"
    else:
        return "Low"

data['date'] = pd.to_datetime(data['date'], errors='coerce')
data['score'] = pd.to_numeric(data['score'], errors='coerce')
data = data.dropna(subset=['score', 'date'])  # Ensure clean data
data['score'] = data['score'].round(1)
data['attendance'] = data['attendance'].astype(str).str.capitalize()
data['categorize_performance'] = data['score'].apply(categorize_score)
data['year_month'] = data['date'].dt.to_period('M')
data['month'] = data['date'].dt.month

load_time = time.time() - start_time

# Sidebar filters
with st.sidebar:
    st.title("Dashboard Controls")
    st.caption(f"Page loaded in **{load_time:.2f}s**")
    if load_time > 3:
        st.warning("⚠️ Load time exceeds 3s target!")
    else:
        st.success("✅ Load time under 3s!")
    
    st.markdown("---")
    
    subjects = ["All"] + sorted(data['subject'].unique().tolist())
    selected_subject = st.selectbox("Select Subject", subjects)
    
    perf_cats = ["All"] + sorted(data['categorize_performance'].unique().tolist())
    selected_perf = st.selectbox("Performance Category", perf_cats)
    
    min_date = data['date'].min().date()
    max_date = data['date'].max().date()
    date_range = st.date_input(
        "Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Apply filters
    filtered_data = data.copy()
    if selected_subject != "All":
        filtered_data = filtered_data[filtered_data['subject'] == selected_subject]
    if selected_perf != "All":
        filtered_data = filtered_data[filtered_data['categorize_performance'] == selected_perf]
    if len(date_range) == 2:
        start, end = date_range
        filtered_data = filtered_data[
            (filtered_data['date'].dt.date >= start) & 
            (filtered_data['date'].dt.date <= end)
        ]

# Dashboard Title
st.title("🎓 Student Performance Dashboard")

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Records", len(filtered_data))
col2.metric("Avg. Score", f"{filtered_data['score'].mean():.1f}" if not filtered_data.empty else "N/A")
col3.metric("Attendance Rate", f"{(filtered_data['attendance'] == 'Present').mean():.1%}" if not filtered_data.empty else "N/A")
col4.metric("High Performers", f"{(filtered_data['categorize_performance'] == 'High').sum()}" if not filtered_data.empty else "0")

st.markdown("---")

# Average Score Trends
st.subheader("📈 Average Score Trends by Subject")
if not filtered_data.empty:
    score_trend = filtered_data.groupby(['year_month', 'subject'])['score'].mean().reset_index()
    score_trend['year_month'] = score_trend['year_month'].astype(str)
    score_trend = score_trend.sort_values('year_month')
    
    if not score_trend.empty:
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        sns.lineplot(data=score_trend, x='year_month', y='score', hue='subject', marker='o', ax=ax1)
        all_months = sorted(score_trend['year_month'].unique())
        if len(all_months) > 6:
            step = max(1, len(all_months) // 6)
            xticks = list(range(0, len(all_months), step))
            xlabels = [all_months[i] for i in xticks]
        else:
            xticks = range(len(all_months))
            xlabels = all_months
        ax1.set_xticks(xticks)
        ax1.set_xticklabels(xlabels, rotation=45)
        ax1.set_title("Monthly Average Scores by Subject")
        st.pyplot(fig1)
    else:
        st.info("No data available for selected filters")
else:
    st.info("No data available")

# Attendance Heatmap
st.subheader("📊 Attendance Rate Heatmap (by Subject & Month)")
if not filtered_data.empty:
    attendance_pivot = filtered_data.pivot_table(
        index='subject',
        columns='month',
        values='attendance',
        aggfunc=lambda x: (x == 'Present').sum() / len(x) if len(x) > 0 else 0
    )
    if not attendance_pivot.empty:
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.heatmap(attendance_pivot, annot=True, fmt=".2f", cmap="Blues", cbar_kws={'label': 'Attendance Rate'}, ax=ax2)
        ax2.set_title("Attendance Rate (%) by Subject and Month")
        ax2.set_xlabel("Month")
        ax2.set_ylabel("Subject")
        st.pyplot(fig2)
    else:
        st.info("No attendance data available")
else:
    st.info("No data available")

# Performance Distribution
st.subheader("📊 Performance Distribution by Subject")
if not filtered_data.empty:
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    sns.countplot(data=filtered_data, y='subject', hue='categorize_performance', palette='Set2', ax=ax3)
    ax3.set_title("Student Performance Levels Across Subjects")
    st.pyplot(fig3)
else:
    st.info("No data available")

# Top 10 High Performers
st.subheader("🏆 Top 10 High Performers (Score ≥ 95)")
top_performers = filtered_data[filtered_data['score'] >= 95].sort_values('score', ascending=False).head(10)
if not top_performers.empty:
    st.dataframe(top_performers[['name', 'subject', 'score', 'attendance']].reset_index(drop=True))
else:
    st.info("No high performers (≥95) in current selection")

# Attendance vs Performance
st.subheader("🔍 Attendance vs Performance Category")
if not filtered_data.empty:
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    sns.countplot(data=filtered_data, x='attendance', hue='categorize_performance', palette='viridis', ax=ax4)
    ax4.set_title("Performance Distribution by Attendance Status")
    st.pyplot(fig4)
else:
    st.info("No data available")

# Final load time
final_load_time = time.time() - start_time
if final_load_time > 3:
    st.sidebar.warning(f"⚠️ Total load time: {final_load_time:.2f}s")
else:
    st.sidebar.success(f"✅ Total load time: {final_load_time:.2f}s")
