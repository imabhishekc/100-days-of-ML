import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# App title and description
st.title('Student Placement Prediction')
st.write('Enter the student\'s CGPA and IQ to predict whether they will be placed.')

# Input fields for CGPA and IQ
cgpa = st.number_input('CGPA', min_value=0.0, max_value=9.0, step=0.1)
iq = st.number_input('IQ', min_value=0, max_value=200, step=1)

# Prediction button
if st.button('Predict'):
    # Create a numpy array from the inputs
    input_data = np.array([[cgpa, iq]])

    # Make prediction
    prediction = model.predict(input_data)

    # Display the result
    if prediction[0] == 1.0:
        st.success('The student will be placed!')
    else:
        st.error('The student will not be placed.')

st.sidebar.info("This is a web app to predict whether a student will get placed based on their CGPA and IQ.")
