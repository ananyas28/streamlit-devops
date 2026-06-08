import streamlit as st

st.title("📜 Log Analyzer")

uploaded_file = st.file_uploader(
    "Upload a log file",
    type=["log", "txt"]
)

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")

    error_count = content.count("ERROR")
    warn_count = content.count("WARN")
    info_count = content.count("INFO")

    st.metric("ERROR", error_count)
    st.metric("WARN", warn_count)
    st.metric("INFO", info_count)

    st.subheader("Log Preview")
    st.text(content[:2000])