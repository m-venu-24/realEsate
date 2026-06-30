import streamlit as st

st.title("Real Estate Investment Recommendation Engine")

st.header("Property Details")

area = st.number_input("Area (sq ft)", min_value=100)

bedrooms = st.number_input("Bedrooms", min_value=1)

bathrooms = st.number_input("Bathrooms", min_value=1)

actual_price = st.number_input(
    "Current Listing Price",
    min_value=1000
)

if st.button("Analyze Property"):
    st.success("Model integration pending...")