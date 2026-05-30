import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Food Delivery Time Predictor")
st.caption("Enter details to predict delivery ETA")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Partner Age", 15, 50, 28)
    rating = st.slider("Partner Rating", 1.0, 6.0, 4.5)
    vehicle = st.selectbox("Vehicle", ["motorcycle","scooter","electric_scooter","bicycle"])

with col2:
    order = st.selectbox("Order Type", ["Meal","Snack","Drinks","Buffet"])
    distance = st.slider("Distance", 0.0, 0.5, 0.1)

vehicle_map = {"bicycle":0,"electric_scooter":1,"motorcycle":2,"scooter":3}
order_map = {"Buffet":0,"Drinks":1,"Meal":2,"Snack":3}
age_group = 0 if age<=25 else (1 if age<=35 else 2)
high_rated = 1 if rating>=4.8 else 0

if st.button("Predict Delivery Time"):
    pred = model.predict([[age, rating, vehicle_map[vehicle],
                          order_map[order], distance, age_group, high_rated]])[0]
    st.success(f"Estimated Time: {pred:.0f} minutes")
    if pred > 35:
        st.warning("High delivery time expected")
    else:
        st.info("Normal delivery time")
