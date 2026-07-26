import streamlit as st
import pandas as pd
import pickle


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="EV Battery Health Prediction",
    page_icon="🔋",
    layout="centered"
)


# -------------------------------
# Load Models
# -------------------------------

@st.cache_resource
def load_models():

    with open("models/soh_model.pkl", "rb") as file:
        soh_model = pickle.load(file)

    with open("models/rul_model.pkl", "rb") as file:
        rul_model = pickle.load(file)

    return soh_model, rul_model


soh_model, rul_model = load_models()


# -------------------------------
# Title
# -------------------------------

st.title("🔋 EV Battery Health Prediction System")

st.write(
    "Predict Battery State of Health (SOH) and Remaining Useful Life (RUL) using XGBoost"
)


st.divider()


# -------------------------------
# Input Section
# -------------------------------

st.subheader("🔧 Enter Battery Parameters")


col1, col2 = st.columns(2)


with col1:

    cycle = st.number_input(
        "Battery Cycle",
        min_value=1,
        max_value=200,
        value=50
    )


    voltage = st.number_input(
        "Voltage",
        min_value=2.5,
        max_value=4.0,
        value=3.5
    )


with col2:

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=60.0,
        value=30.0
    )


    capacity = st.number_input(
        "Capacity",
        min_value=0.5,
        max_value=3.0,
        value=1.5
    )


st.divider()


# -------------------------------
# Prediction
# -------------------------------

if st.button("🔍 Predict Battery Health"):


    # SOH Prediction Input

    soh_input = pd.DataFrame({

        "cycle": [cycle],
        "voltage": [voltage],
        "temperature": [temperature],
        "capacity": [capacity]

    })


    predicted_soh = soh_model.predict(
        soh_input
    )[0]


    # RUL Prediction Input

    rul_input = pd.DataFrame({

        "cycle": [cycle],
        "voltage": [voltage],
        "temperature": [temperature],
        "capacity": [capacity],
        "predicted_soh": [predicted_soh]

    })


    predicted_rul = rul_model.predict(
        rul_input
    )[0]


    # -------------------------------
    # Results
    # -------------------------------

    st.success("Prediction Completed")


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            label="🔋 Battery SOH",
            value=f"{predicted_soh*100:.2f}%"
        )


    with col2:

        st.metric(
            label="⏳ Remaining Useful Life",
            value=f"{predicted_rul:.0f} cycles"
        )


    st.divider()


    # -------------------------------
    # Battery Status
    # -------------------------------

    st.subheader("Battery Condition")


    if predicted_soh >= 0.80:

        st.success(
            "🟢 Healthy Battery"
        )


    elif predicted_soh >= 0.60:

        st.warning(
            "🟡 Moderate Battery"
        )


    else:

        st.error(
            "🔴 Critical Battery"
        )