import streamlit as st
import psutil
import pandas as pd

st.title("📊 Process Monitor")

processes = []

for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    try:
        processes.append(proc.info)
    except:
        pass

df = pd.DataFrame(processes)

if not df.empty:
    df = df.sort_values(by='cpu_percent', ascending=False).head(10)

st.subheader("Top 10 CPU Consuming Processes")
st.dataframe(df)