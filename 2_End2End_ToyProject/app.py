import streamlit as st
import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set the page title and header
st.title('Student Placement Prediction')
st.header('Enter Student Details')

# Create input fields for IQ and CGPA
iq = st.number_input('IQ')
cgpa = st.number_input('CGPA')

# Create a button to make predictions
if st.button('Predict'):
    # Prepare the input data for the model
    input_data = [[iq, cgpa]]

    # Make a prediction
    prediction = model.predict(input_data)

    # Display the prediction
    if prediction[0] == 1:
        st.success('This student is likely to get placed.')
    else:
        st.error('This student is not likely to get placed.')