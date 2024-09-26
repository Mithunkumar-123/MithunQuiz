# prompt: make app with streamlit app for rf model

import streamlit as st
import pandas as pd
import pickle

# Load the trained Random Forest model
filename = 'rf_model.pkl'
rf_model = pickle.load(open(filename, 'rb'))

# Create a Streamlit app
st.title("Monthly Revenue Prediction App")

# Create input fields for features
st.header("Enter Store Information")

# Example: Assuming your features are 'website_traffic', 'avg_order_value', 'customer_acquisition_cost'
website_traffic = st.number_input("Website Traffic", min_value=0)
avg_order_value = st.number_input("Average Order Value", min_value=0.0)
customer_acquisition_cost = st.number_input("Customer Acquisition Cost", min_value=0.0)

# Create a button to make predictions
if st.button("Predict Monthly Revenue"):
    # Create a DataFrame with user input
    input_data = pd.DataFrame({
        'website_traffic': [website_traffic],
        'avg_order_value': [avg_order_value],
        'customer_acquisition_cost': [customer_acquisition_cost]
        # Add more features as needed
    })

    # Make predictions using the loaded model
    predicted_revenue = rf_model.predict(input_data)[0]

    # Display the prediction
    st.subheader("Predicted Monthly Revenue:")
    st.write(f"${predicted_revenue:.2f}") 