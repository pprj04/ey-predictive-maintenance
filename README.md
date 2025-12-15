# 🚗 AI-Powered Predictive Maintenance System  
**EY Techathon 6.0 | Automotive Industry Challenge**

---

## 📌 Project Overview
Modern vehicles still rely heavily on reactive maintenance, which leads to unexpected breakdowns, increased repair costs, and poor customer experience.  
This project presents an **AI-powered Predictive Maintenance System** that leverages **telematics data, agentic AI orchestration, and UEBA monitoring** to proactively predict failures, auto-schedule service, and provide root cause insights to OEMs.

The solution is implemented as a **working Streamlit prototype** using synthetic telematics data and is fully aligned with EY Techathon guidelines.

---

## 🎯 Key Objectives
- Predict potential vehicle failures before breakdown  
- Automate service scheduling without manual intervention  
- Provide RCA insights to manufacturing and quality teams  
- Ensure secure and governed AI actions using UEBA  
- Demonstrate an end-to-end Agentic AI workflow  

---

## 🧠 Solution Highlights
- **Predictive Analytics:** Failure probability based on vehicle telemetry  
- **Agentic AI:** Master Agent coordinating multiple Worker Agents  
- **RCA Dashboard:** Fleet-level insights for OEM improvement  
- **UEBA Monitoring:** Detects anomalous agent behavior  
- **No Hardware Dependency:** Uses synthetic telematics data  

---

## 🏗️ High-Level Architecture
1. Telematics Data Ingestion (Synthetic CSV)  
2. Data Processing & Feature Analysis  
3. Failure Prediction Engine  
4. Master Agent Orchestration  
5. Worker Agents:
   - Diagnosis Agent  
   - Scheduling Agent  
   - Customer Engagement Agent  
   - RCA Agent  
   - UEBA Security Agent  
6. Web-Based Dashboard (Streamlit)

---

## 🖥️ Prototype Features
The working prototype demonstrates:
- Vehicle telemetry dashboard  
- Failure probability visualization  
- Auto-service scheduling workflow  
- RCA insights using bar charts  
- UEBA anomaly detection logs  

(Screenshots included in PPT submission.)

---

## 🛠️ Tech Stack
- **Language:** Python  
- **UI Framework:** Streamlit  
- **Data Handling:** Pandas, NumPy  
- **Prediction Logic:** Rule-based / lightweight ML  
- **Visualization:** Streamlit charts  
- **Security Concept:** UEBA (User & Entity Behavior Analytics)  
- **Data Source:** Synthetic telematics CSV  

---

## 📁 Project Structure
ey_prototype/
├── app.py
├── data/
│ └── telematics.csv
├── utils/
│ ├── predictor.py
│ ├── scheduler.py
│ └── ueba.py
├── requirements.txt
└── README.md

---

## ▶️ How to Run the Prototype

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

2️⃣ Run the Streamlit application
python -m streamlit run app.py

3️⃣ Open in browser
http://localhost:8501

📊 Sample Output

Failure probability (%) for selected vehicle

Fleet-level RCA bar charts

UEBA logs highlighting anomalous actions

🔐 Security & Governance

The solution integrates a UEBA layer to monitor agent behavior, detect anomalies such as unauthorized access, and ensure responsible autonomous execution.

🚀 Future Enhancements

Integration with real-time IoT telematics streams

Advanced ML / Deep Learning models

Voice-based customer interaction

Cloud deployment with scalable pipelines

Integration with OEM ERP and service systems

🏆 EY Techathon Context

This project was developed for EY Techathon 6.0 – Automotive Predictive Maintenance Challenge, showcasing innovation in Agentic AI, predictive analytics, and secure autonomous systems.

👥 Team

Team Name: Spacemates
Project: AI-Powered Predictive Maintenance & Agentic Scheduling System
