import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

# Title
st.title("🎓 Student Creditworthiness Predictor")

st.markdown("Enter the student's academic and financial details:")

# Input fields
gpa = st.number_input("GPA", min_value=0.0, max_value=10.0, step=0.1)
online_txn = st.number_input("Monthly Online Transactions", min_value=0, step=1)
monthly_income = st.number_input("Monthly Income (₹)", min_value=0, step=100)
age = st.number_input("Age", min_value=16, max_value=30, step=1)
branch = st.selectbox("Branch", ["CSE", "ECE", "ME", "CE", "EE"])
attendance = st.slider("Attendance Percent", 0, 100, step=1)
part_time = st.selectbox("Part-Time Work", ["Yes", "No"])
credit_score = st.number_input("Credit Score (0-1000)", min_value=0, max_value=1000, step=1)

# Encoding maps (as used in your training)
branch_map = {"CSE": 0, "ECE": 1, "ME": 2, "CE": 3, "EE": 4}
part_time_map = {"Yes": 1, "No": 0}

# Predict
if st.button("Predict"):
    input_data = np.array([[
        gpa,
        online_txn,
        monthly_income,
        age,
        branch_map[branch],
        attendance,
        part_time_map[part_time],
        credit_score
    ]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ The student is Creditworthy")
    else:
        st.error("❌ The student is NOT Creditworthy")
