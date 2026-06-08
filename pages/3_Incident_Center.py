import streamlit as st
import psutil

st.title("🚨 Incident Center")

cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

incidents = []

if cpu > 80:
    incidents.append(f"High CPU Usage: {cpu}%")

if memory > 85:
    incidents.append(f"High Memory Usage: {memory}%")

if disk > 90:
    incidents.append(f"High Disk Usage: {disk}%")

if incidents:
    st.error("Active Incidents Detected")

    for incident in incidents:
        st.write("🔴", incident)

else:
    st.success("No Active Incidents")