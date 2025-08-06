import streamlit as st

def job_matching_page():
    st.title("AI Job Matching")
    st.text_input("Enter your primary skill", key="skill_input")
    if st.button("Find Jobs"):
        st.success("Top Matching Jobs:")
        st.markdown("- Data Analyst at ABC Corp")
        st.markdown("- Machine Learning Intern at XYZ Ltd.")
