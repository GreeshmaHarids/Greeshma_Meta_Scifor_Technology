import streamlit as st



if st.text_input("Enter your Name:",key="name"):
    st.write(f"Hi....",st.session_state.name)