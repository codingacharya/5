import streamlit as st
from utils.auth import login_signup
from pages.resume_screening import resume_screening_page
from pages.job_matching import job_matching_page
from pages.career_counseling import career_counseling_page

st.set_page_config(page_title="AI Job Portal", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login/Signup", "Resume Screening", "Job Matching", "Career Counseling"])

if page == "Login/Signup":
    login_signup()
elif page == "Resume Screening":
    resume_screening_page()
elif page == "Job Matching":
    job_matching_page()
elif page == "Career Counseling":
    career_counseling_page()
