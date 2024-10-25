import streamlit as st

st.title("Hello....Find Out Your BMI \nAre You in the Healthy Range?")

def calculate_bmi():
    weight = st.session_state['weight']
    height = st.session_state['height']

    
    # Check if inputs are valid numbers
    try:
        weight = float(weight) 
        height = float(height)  

        if height > 0:  
            bmi = weight / (height ** 2)  # BMI formula
            st.write(f"Your BMI is: {bmi:.2f}")
            if bmi < 18.5:
                st.write("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.write("You are in the normal weight range.")
            elif 25 <= bmi < 29.9:
                st.write("You are overweight.")
            else:
                st.write("You are obese.")
            
            st.write("**Keep tracking your BMI and stay healthy!**")
        else:
            st.write("Height must be greater than zero.")
    except ValueError:
        st.write("Please enter valid numbers for both weight and height.")

st.text_input("Enter your weight (kg):", key="weight")
st.text_input("Enter your height (m):", key="height")

# Button to trigger BMI calculation
if st.button("Calculate BMI"):
    calculate_bmi()
