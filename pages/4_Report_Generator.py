import streamlit as st
import psutil
import pandas as pd
from datetime import datetime

st.title("📄 Report Generator")

cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

health_score = 100

if cpu > 80:
    health_score -= 30

if memory > 85:
    health_score -= 30

if disk > 90:
    health_score -= 40

report = pd.DataFrame({
    "Timestamp": [datetime.now()],
    "CPU Usage (%)": [cpu],
    "Memory Usage (%)": [memory],
    "Disk Usage (%)": [disk],
    "Health Score": [health_score]
})

st.dataframe(report)

csv = report.to_csv(index=False)

st.download_button(
    label="📥 Download Health Report",
    data=csv,
    file_name="health_report.csv",
    mime="text/csv"
)