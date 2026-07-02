import streamlit as st
import pandas as pd
import joblib

from recommendation import get_recommendation

# Load trained model
model = joblib.load("models/model.pkl")

st.title("🏠 Real Estate Investment Recommendation Engine")

st.header("Property Details")

bedrooms = st.number_input("Bedrooms", min_value=1, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, value=2)
sqft_living = st.number_input("Living Area (sqft)", min_value=500, value=2000)

actual_price = st.number_input(
    "Current Listing Price (₹)",
    min_value=10000,
    value=500000
)

if st.button("Analyze Property"):

    input_data = pd.DataFrame([{
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'sqft_living': sqft_living,
        'sqft_lot': 5000,
        'floors': 2,
        'waterfront': 0,
        'view': 0,
        'condition': 3,
        'grade': 7,
        'sqft_above': sqft_living,
        'sqft_basement': 0,
        'yr_built': 2000,
        'yr_renovated': 0,
        'zipcode': 98001,
        'lat': 47.5,
        'long': -122.2,
        'sqft_living15': sqft_living,
        'sqft_lot15': 5000,
        'year': 2014,
        'month': 6,
        'house_age': 14,
        'renovated': 0
    }])

    predicted_price = model.predict(input_data)[0]

    score = predicted_price / actual_price

    recommendation = get_recommendation(score)

    st.subheader("Results")

    st.write(f"Predicted Market Price: ₹{predicted_price:,.2f}")
    st.write(f"Investment Score: {score:.2f}")

    st.success(f"Recommendation: {recommendation}")