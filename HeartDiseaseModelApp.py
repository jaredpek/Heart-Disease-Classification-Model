import streamlit as st
import pandas as pd
from joblib import load

title = st.title("Heart Disease Prediction")
hdModel = load(filename="HeartDiseaseModel.joblib")


def make_prediction(input_data):
    prediction = hdModel.predict(input_data)
    print(prediction)

    if prediction == 1:
        st.error("Heart Disease")
        return "Heart Disease"

    elif prediction == 0:
        st.success("No Heart Disease")
        return "No Heart Disease"

    else:
        st.warning("Error Has Occurred")
        return "Error"


sex_list = ["Male", "Female"]
cp_list = ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"]
restecg_list = ["Normal", "Abnormality Found"]
exang_list = ["Yes", "No"]
slope_list = ["Upsloping", "Flat", "Downsloping"]
thal_list = ["None", "Normal", "Fixed Defect", "Reversible Defect"]
index_list = ["age", "sex", "cp", "trestbps", "chol", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]


with st.form("heart_disease_prediction"):
    age = st.number_input("Age", 1, 150)
    sex = sex_list.index(st.selectbox("Gender", sex_list))
    cp = cp_list.index(st.selectbox("Chest Pain Type", cp_list))
    trestbps = st.number_input("Resting Blood Pressure in mmHg", 1, 300)
    chol = st.number_input("Cholestrol Level", 1, 500)
    restecg = restecg_list.index(st.selectbox("Resting ECG Result", restecg_list))
    thalach = st.number_input("Maximum Heart Rate", 1, 300)
    exang = exang_list.index(st.selectbox("Exercise Induced Angina", exang_list))
    oldpeak = st.number_input("ST Depression Induced by Exercise relative to Rest", 0.0, 10.0, step=0.1)
    slope = slope_list.index(st.selectbox("Slope of Peak Exercise ST Segment", slope_list))
    ca = st.number_input("Number of Major Vessels Colored by Flouroscopy", 0, 10)
    thal = thal_list.index(st.selectbox("Thalassemia State", thal_list))
    submitted = st.form_submit_button("Predict")

    if submitted:
        input_data = pd.DataFrame([age, sex, cp, trestbps, chol, restecg, thalach, exang, oldpeak, slope, ca, thal], index=index_list).transpose()
        make_prediction(input_data)
