🚗 AI-Powered Predictive Maintenance System

EY Techathon 6.0 | Automotive Industry Challenge

📌 Project Overview

Modern vehicles still rely heavily on reactive maintenance, leading to unexpected breakdowns, higher repair costs, and poor customer experience.
This project presents an AI-powered Predictive Maintenance System that uses telematics data, agentic AI orchestration, and UEBA monitoring to proactively predict failures, schedule service, and provide root cause insights to OEMs.

The solution is built as a working Streamlit prototype using synthetic data, fully aligned with EY Techathon guidelines.

🎯 Key Objectives

Predict potential vehicle failures before breakdown

Automate service scheduling without manual intervention

Provide RCA insights to manufacturing and quality teams

Ensure secure and governed AI actions using UEBA

Demonstrate an end-to-end Agentic AI workflow

🧠 Solution Highlights

Predictive Analytics: Failure probability based on telemetry patterns

Agentic AI: Master Agent orchestrating diagnosis, scheduling, RCA, and engagement

RCA Dashboard: Fleet-level insights for OEM quality improvement

UEBA Monitoring: Detects anomalous agent behavior

No Hardware Required: Uses synthetic telematics data

🏗️ System Architecture (High Level)

Telematics Data Ingestion (Synthetic)

Data Processing & Feature Extraction

Failure Prediction Engine

Master Agent Orchestration

Worker Agents:

Diagnosis Agent

Scheduling Agent

Customer Engagement Agent

RCA Agent

UEBA Security Agent

Web-based Dashboard (Streamlit)

🖥️ Prototype Screens

The working prototype demonstrates:

Vehicle telemetry dashboard

Failure probability visualization

Auto-service scheduling flow

RCA insights using charts

UEBA anomaly detection logs

(All screenshots included in the PPT submission.)

🛠️ Tech Stack

Language: Python

UI Framework: Streamlit

Data Handling: Pandas, NumPy

Prediction Logic: Rule-based / lightweight ML

Visualization: Streamlit charts

Security Concept: UEBA (User & Entity Behavior Analytics)

Data Source: Synthetic CSV telematics data

📁 Project Structure
ey_prototype/
├── app.py
├── data/
│   └── telematics.csv
├── utils/
│   ├── predictor.py
│   ├── scheduler.py
│   └── ueba.py
├── requirements.txt
└── README.md

▶️ How to Run the Prototype
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit app
python -m streamlit run app.py

3️⃣ Open in browser
http://localhost:8501

📊 Sample Output

Failure Probability (%) for selected vehicle

RCA bar charts across fleet

UEBA logs highlighting anomalous actions

🔐 Security & Governance

The system integrates a UEBA layer to monitor agent behavior, detect anomalies (e.g., bulk data access), and ensure responsible AI execution.

🚀 Future Enhancements

Integration with real-time IoT telematics APIs

Advanced ML/DL models for prediction

Voice-based customer interaction

Cloud deployment with scalable data pipelines

Integration with OEM ERP & service systems

🏆 EY Techathon Context

This project was developed as part of EY Techathon 6.0 – Automotive Predictive Maintenance Challenge and demonstrates innovation in Agentic AI, predictive analytics, and secure autonomous systems.

👤 Team

Team Name: Spacemates
Role: AI-Powered Predictive Maintenance Solution
