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

#eg for bar chart
import matplotlib.pyplot as plt

# Sample data
data = {'A': 30, 'B': 40, 'C': 50}

# Create a bar chart
st.header("Bar Chart Example")
plt.bar(data.keys(), data.values())
st.pyplot(plt)

#eg for pie chart

pie_data = {
    'Red': 40,
    'Blue': 30,
    'Green': 20,
    'Yellow': 10
}
st.header("Color Distribution Pie Chart")
plt.pie(pie_data.values(), labels=pie_data.keys(), autopct='%1.1f%%', startangle=90)
plt.title('Color Distribution')
st.pyplot(plt)



