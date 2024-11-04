import streamlit as st

# Checkbox for selecting filters
filter_selected = st.checkbox("Select Filters")
if filter_selected:
    st.write("Selected filters")
else:
    st.write("No filters selected")

# Function to display the home page
def home():
    st.write("This is the home page")

# Function to display the second page
def second():
    st.write("This is the second page")

# Buttons to navigate between pages
if st.button("Home"):
    home()
if st.button("Second Page"):
    second()
