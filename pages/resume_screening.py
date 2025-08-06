import streamlit as st

def resume_screening_page():
    st.title("AI Resume Screening")
    uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    if uploaded_file:
        st.success("Resume uploaded!")
        st.info("AI Feedback:")
        st.markdown("- Add more keywords related to Data Science")
        st.markdown("- Improve formatting in the experience section")
