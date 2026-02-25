import streamlit as st
import requests

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

# --- API Request Function ---
def predict_bp(data):
    url = "https://api.groa.io/predict"  # Make sure this URL is correct
    
    headers = {
        "Authorization": "Bearer YOUR_REAL_API_KEY",  # Replace with your actual key
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API Error {response.status_code}: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        st.error(f"Connection Error: {e}")
        return None


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