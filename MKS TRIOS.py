import streamlit as st

# --- Streamlit App Title ---
st.title("PulseGuard AI – Blood Pressure Prediction")

# --- User Input Section ---
st.header("Enter Patient Data")

age = st.number_input("Age", min_value=1, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
smoking = st.selectbox("Smoking Habit", ["Non-smoker", "Smoker"])
exercise = st.selectbox("Exercise Frequency", ["Low", "Moderate", "High"])
stress = st.selectbox("Stress Level", ["Low", "Moderate", "High"])

# --- Convert to numeric (Safe for most ML APIs) ---
smoking_map = {"Non-smoker": 0, "Smoker": 1}
exercise_map = {"Low": 0, "Moderate": 1, "High": 2}
stress_map = {"Low": 0, "Moderate": 1, "High": 2}

payload = {
    "age": age,
    "bmi": bmi,
    "smoking": smoking_map[smoking],
    "exercise": exercise_map[exercise],
    "stress": stress_map[stress]
}

# --- Local Prediction Function (No External API) ---
def predict_bp(data):
    """Local prediction function that calculates BP stage based on patient data"""
    age = data["age"]
    bmi = data["bmi"]
    smoking = data["smoking"]
    exercise = data["exercise"]
    stress = data["stress"]
    
    # Calculate risk score based on factors
    risk_score = 0.3
    
    # Age factor
    if age > 60:
        risk_score += 0.15
    elif age > 45:
        risk_score += 0.10
    
    # BMI factor
    if bmi > 30:
        risk_score += 0.15
    elif bmi > 25:
        risk_score += 0.08
    
    # Smoking factor
    if smoking == 1:
        risk_score += 0.20
    
    # Exercise factor
    if exercise == 0:
        risk_score += 0.10
    
    # Stress factor
    if stress == 2:
        risk_score += 0.12
    elif stress == 1:
        risk_score += 0.06
    
    # Cap risk score
    risk_score = min(risk_score, 0.99)
    
    # Determine stage
    if risk_score < 0.5:
        stage = "Normal"
    elif risk_score < 0.65:
        stage = "Elevated"
    elif risk_score < 0.80:
        stage = "Stage 1 Hypertension"
    else:
        stage = "Stage 2 Hypertension"
    
    return {
        "predicted_stage": stage,
        "risk_score": round(risk_score, 2)
    }


# --- Prediction Button ---
if st.button("Predict Blood Pressure Stage"):
    with st.spinner("Analyzing patient data..."):
        result = predict_bp(payload)

        if result:
            st.success("Prediction Successful!")

            st.subheader("Predicted Stage:")
            st.write(result.get("predicted_stage", "N/A"))

            st.subheader("Risk Score:")
            st.write(result.get("risk_score", "N/A"))

            st.subheader("Recommended Actions:")
            recommendations = result.get("recommendations", [])

            if recommendations:
                for action in recommendations:
                    st.write(f"- {action}")
            else:
                st.write("No recommendations provided.")