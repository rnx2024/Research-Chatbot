# insightful_streamlit_app.py (Refactored + Enhanced UI)

import streamlit as st
from datetime import datetime, timedelta
from fetch_data import fetch_data
from gpt_analysis import (
    analyze_behavioral_trends,
    analyze_productivity_bottlenecks,
    analyze_performance_forecasts,
    analyze_task_allocation_strategy,
    summarize_team_with_gpt
)
import pandas as pd
import os

# Page setup
st.set_page_config(page_title="AI-Powered Productivity Analysis", layout="centered")
st.markdown("""
<style>
    .main-box {
        background-color: #f8f9fa;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    div[data-testid="stChatInput"] textarea {
        border: 2px solid #90EE90 !important;
        border-radius: 5px;
    }
</style>
<div class="main-box">
""", unsafe_allow_html=True)

st.title("📊 OpenAI Employee Productivity Reports")
st.markdown("_by Rhanny_AITeam_", unsafe_allow_html=True)

# Date setup
yesterday = (datetime.utcnow() - timedelta(days=1)).strftime("%A, %B %d, %Y")
st.markdown(f"📅 **Data Date**: _{yesterday}_")

# Session state initialization
if "dataframes" not in st.session_state:
    st.session_state["dataframes"] = None
    st.session_state["team_summaries"] = None

# Fetch data button
if st.button(f"📥 Fetch Insightful Data ({yesterday})"):
    st.info("Pulling data and performing screenshot OCR analysis...")
    try:
        dataframes, team_summaries = fetch_data()
        st.session_state["dataframes"] = dataframes
        st.session_state["team_summaries"] = team_summaries
        st.success("✅ Data fetched and team summaries ready.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# If data is available, allow GPT analysis
if st.session_state["dataframes"] is not None:
    st.subheader("🧠 Generate Organization-Level GPT Insights")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧠 Behavioral Trends"):
            st.info("Analyzing behavior trends...")
            st.write(analyze_behavioral_trends(st.session_state["dataframes"]))

        if st.button("📈 Performance Forecasts"):
            st.info("Forecasting performance...")
            st.write(analyze_performance_forecasts(st.session_state["dataframes"]))

    with col2:
        if st.button("🚨 Productivity Bottlenecks"):
            st.info("Checking for bottlenecks...")
            st.write(analyze_productivity_bottlenecks(st.session_state["dataframes"]))

        if st.button("🗂️ Task Allocation Strategy"):
            st.info("Analyzing task allocation...")
            st.write(analyze_task_allocation_strategy(st.session_state["dataframes"]))

# Per-Team GPT Summary Dropdown
if "team_summaries" in st.session_state and st.session_state["team_summaries"]:
    st.subheader("📂 Team-Based GPT Summary")
    team_ids = list(st.session_state["team_summaries"].keys())
    selected_team = st.selectbox("Select a team:", team_ids)

    if st.button("🤖 Analyze Selected Team with GPT"):
        summary = st.session_state["team_summaries"][selected_team]
        st.write(summarize_team_with_gpt(summary))

    if st.button("💾 Export This Team's Summary"):
        os.makedirs("exports", exist_ok=True)
        summary = st.session_state["team_summaries"][selected_team]
        df = pd.DataFrame([summary])
        file_path = f"exports/{selected_team}_summary.csv"
        df.to_csv(file_path, index=False)
        st.success(f"✅ Saved to {file_path}")

st.markdown("""</div>""", unsafe_allow_html=True)
