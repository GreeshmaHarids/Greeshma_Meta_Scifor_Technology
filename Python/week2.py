# Eg for all questions related to streamlit

#5
import streamlit as st

st.write("Question no.5")
st.divider()

st.button("Click Here")
st.slider("Number Range",0,100)
st.text_input("Enter Your Name:")

st.write("Question no.6")
st.divider()

st.write("In Streamlit, sessions keep track of variables and app states (e.g., counters, form inputs) so that values don’t reset with every interaction using st.session_state, allowing data to persist across app reruns.")

if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button('Increment'):
    st.session_state.count += 1

st.write("Count:", st.session_state.count)



st.write("Question no.7")
st.divider()
st.write("Using *streamlit run filename.py* in the terminal.(where *filename.py* is the name of the file with code)")

st.write("Question no.8")
st.divider()

import streamlit as st
import matplotlib.pyplot as plt

# Sample data for bar chart
bar_data = {
    'Category A': 25,
    'Category B': 40,
    'Category C': 35
}

# Sample data for pie chart
pie_data = {
    'Slice 1': 15,
    'Slice 2': 25,
    'Slice 3': 60
}

# Sidebar to select the chart type
chart_type = st.sidebar.selectbox("Select chart type:", ["Bar Chart", "Pie Chart"])

if chart_type == "Bar Chart":
    st.header("Bar Chart Example")
    plt.bar(bar_data.keys(), bar_data.values(), color='skyblue')
    plt.title('Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    st.pyplot(plt)

elif chart_type == "Pie Chart":
    st.header("Pie Chart Example")
    plt.pie(pie_data.values(), labels=pie_data.keys(), autopct='%1.1f%%', startangle=90)
    plt.title('Pie Chart')
    st.pyplot(plt)
