import streamlit as st
import psutil
import platform
import socket
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
st.set_page_config(
    page_title="DevOps Monitoring Dashboard",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 DevOps Monitoring Dashboard")

st.markdown("---")

# System Information
st.header("🖥️ System Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Hostname:**", socket.gethostname())
    st.write("**Operating System:**", platform.system())
    st.write("**Release:**", platform.release())

with col2:
    st.write("**Processor:**", platform.processor())
    st.write("**Python Version:**", platform.python_version())

st.markdown("---")

# Metrics
cpu = psutil.cpu_percent()
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPU Usage", f"{cpu}%")

with col2:
    st.metric("Memory Usage", f"{memory.percent}%")

with col3:
    st.metric("Disk Usage", f"{disk.percent}%")

st.markdown("---")
data = pd.DataFrame({
    "Metric": ["CPU", "Memory", "Disk"],
    "Usage": [cpu, memory.percent, disk.percent]
})

fig = px.bar(
    data,
    x="Metric",
    y="Usage",
    title="Infrastructure Resource Usage"
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")
st.header("🏥 Infrastructure Health Score")

health_score = 100

if cpu > 80:
    health_score -= 30

if memory.percent > 85:
    health_score -= 30

if disk.percent > 90:
    health_score -= 40

st.metric("Health Score", f"{health_score}/100")

if health_score >= 90:
    st.success("🟢 Healthy Infrastructure")
elif health_score >= 70:
    st.warning("🟡 Moderate Risk")
else:
    st.error("🔴 Critical Infrastructure State")
# Health Check
st.header("🚨 Health Status")

if cpu > 80 or memory.percent > 85 or disk.percent > 90:
    st.error("Critical Resource Usage Detected!")
elif cpu > 60 or memory.percent > 70:
    st.warning("System Under Moderate Load")
else:
    st.success("System Healthy")
    import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=health_score,
    title={'text': "Infrastructure Health"},
    gauge={'axis': {'range': [0, 100]}}
))

st.plotly_chart(fig, use_container_width=True)