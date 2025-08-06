import streamlit as st

def login_signup():
    st.title("Login / Signup")
    tab1, tab2 = st.tabs(["Login", "Signup"])
    with tab1:
        st.text_input("Username", key="login_user")
        st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            st.success("Logged in successfully")
    with tab2:
        st.text_input("New Username", key="signup_user")
        st.text_input("New Password", type="password", key="signup_pass")
        if st.button("Signup"):
            st.success("Account created")
