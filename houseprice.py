import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("house_price_model.pkl")

model = load_model()

# Streamlit UI
st.title("🏠 House Price Predictor")
st.write("Enter the details below to estimate the house price:")

# Input sliders
area = st.number_input("Area (in square feet)", min_value=100, max_value=10000, value=1500)
bedrooms = st.number_input("Number of bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of bathrooms", min_value=1, max_value=10, value=2)

# Prediction
if st.button("Predict Price"):
    input_data = pd.DataFrame([[area, bedrooms, bathrooms]], columns=['Area', 'Bedrooms', 'Bathrooms'])
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted Price: ₹{int(prediction):,}")
