import streamlit as st

# App Title
st.title("PulseGuard AI – Blood Pressure Prediction")

# Input Section
st.header("Enter Patient Data")

age = st.number_input("Age", min_value=1, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
smoking = st.selectbox("Smoking Habit", ["Non-smoker", "Smoker"])
exercise = st.selectbox("Exercise Frequency", ["Low", "Moderate", "High"])
stress = st.selectbox("Stress Level", ["Low", "Moderate", "High"])

# Button
if st.button("Predict Blood Pressure Stage"):
    st.success("Prediction Successful 🔥")
    st.write("### Predicted Stage:")
    st.write("Stage 1 Hypertension")
    st.write("### Risk Score:")
    st.write("0.78")
    st.write("### Recommended Actions:")
    st.write("- Exercise regularly")
    st.write("- Reduce salt intake")
    st.write("- Manage stress")