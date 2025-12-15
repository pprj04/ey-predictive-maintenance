import os
import streamlit as st
import pandas as pd
from utils.predictor import predict_failure
from utils.scheduler import auto_schedule
from utils.ueba import get_logs

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "telematics.csv")

st.set_page_config(page_title="Predictive Maintenance AI", layout="wide")

st.title("🚗 AI-Powered Predictive Maintenance System")

df = pd.read_csv(DATA_PATH)
vehicle = st.selectbox("Select Vehicle", df["vehicle_id"])

row = df[df["vehicle_id"] == vehicle].iloc[0]

st.subheader("Vehicle Telemetry")
st.write(row)

risk = predict_failure(row.engine_temp, row.rpm, row.battery_voltage)

st.subheader("Failure Probability")
st.progress(risk)
st.write(f"Risk Level: **{risk}%**")

if risk > 60:
    st.error("⚠️ High Failure Probability Detected")

    if st.button("Auto-Schedule Service"):
        schedule = auto_schedule(vehicle)
        st.success(f"""
        ✅ Service Scheduled  
        📅 {schedule['date']}  
        ⏰ {schedule['time']}  
        🏢 {schedule['service_center']}
        """)

st.subheader("📊 RCA Insights")
st.bar_chart(df.groupby("vehicle_id")["engine_temp"].mean())

st.subheader("🔐 UEBA Monitoring")
logs = get_logs()
for log in logs:
    if log[2] == "ANOMALOUS":
        st.error(f"{log[0]} – {log[1]} – {log[2]}")
    else:
        st.success(f"{log[0]} – {log[1]} – {log[2]}")
