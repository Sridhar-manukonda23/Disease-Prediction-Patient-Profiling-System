# 🩺 Disease Prediction & Patient Profiling System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-success)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-Educational-green)

### AI-Powered Healthcare Web Application using Machine Learning

Predict diseases based on symptoms, manage patient records, and generate professional PDF medical reports.

🌐 **Live Demo:** https://disease-prediction-patient-profiling-xedy.onrender.com

</div>

---

# 📌 Overview

Disease Prediction & Patient Profiling System is a Machine Learning-powered healthcare web application developed using **Python**, **Flask**, **SQLite**, and **Scikit-learn**.

The application predicts the **Top 3 most probable diseases** based on user-selected symptoms using a trained **Random Forest Classifier**. It also provides disease descriptions, precautions, patient history management, dashboard analytics, and downloadable PDF reports.

> **Disclaimer:** This project is intended for educational and demonstration purposes only and should not replace professional medical advice.

---

# 🚀 Live Demo

### 🌍 Website

https://disease-prediction-patient-profiling-xedy.onrender.com

---

# ✨ Features

## 🤖 AI Disease Prediction

- Predict diseases using Machine Learning
- Random Forest Classification
- Top 3 predictions
- Confidence percentage
- Fast prediction results

---

## 👤 Patient Management

- Patient Registration
- Age & Gender Details
- Symptom Selection
- Patient History

---

## 📊 Dashboard

- Total Patients
- Total Predictions
- Disease Statistics
- Interactive Dashboard

---

## 📄 PDF Report

Generate downloadable reports containing:

- Patient Information
- Predicted Disease
- Confidence Score
- Disease Description
- Precautions
- Date & Time

---

## 📂 Patient History

- View previous records
- Search patient history
- Delete records

---

## 🎨 Modern UI

- Responsive Design
- Bootstrap 5
- Interactive Dashboard
- Searchable Symptoms
- AI Loading Screen
- Professional Navigation

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|-------------|
| Language | Python |
| Backend | Flask |
| Machine Learning | Random Forest, Scikit-learn |
| Database | SQLite |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Libraries | Pandas, Joblib, ReportLab |

---

# 🧠 Machine Learning Workflow

```text
Symptoms
      │
      ▼
Data Preprocessing
(MultiLabelBinarizer)
      │
      ▼
Random Forest Model
      │
      ▼
Disease Prediction
      │
      ▼
Top 3 Diseases
      │
      ▼
PDF Report
```

---

# 🏗️ System Architecture

```text
                User
                  │
                  ▼
        Flask Web Application
                  │
     ┌────────────┴────────────┐
     ▼                         ▼
Machine Learning          SQLite Database
(Random Forest)         Patient Records
     │
     ▼
Prediction Result
     │
     ▼
PDF Report Generation
```

---

# 📁 Project Structure

```text
Disease_Prediction_System/

│── app.py
│── train_model.py
│── database.py
│── pdf_generator.py
│── disease_model.pkl
│── symptom_encoder.pkl
│── patient_history.db
│── requirements.txt
│── runtime.txt

├── dataset/

├── static/
│   ├── css/
│   ├── js/
│   └── images/

└── templates/
    ├── index.html
    ├── result.html
    ├── dashboard.html
    ├── history.html
    ├── loading.html
    └── base.html
```

---

# 📸 Screenshots

Add screenshots here.

Example:

```
screenshots/
│── home.png
│── prediction.png
│── dashboard.png
│── history.png
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Sridhar-manukonda23/Disease-Prediction-Patient-Profiling-System.git
```

### Navigate

```bash
cd Disease-Prediction-Patient-Profiling-System
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

# 🎯 Future Enhancements

- User Authentication
- Doctor Recommendation
- Hospital API Integration
- Mobile Application
- Cloud Database
- Email Reports
- Appointment Booking
- Multilingual Support

---

# 👨‍💻 Developer

## Manukonda Sridhar

**B.Tech - Computer Science & Engineering**

📍 Raghu Engineering College

### Connect with Me

- 🔗 GitHub: https://github.com/Sridhar-manukonda23
- 💼 LinkedIn: https://www.linkedin.com/in/manukonda-sridhar-9b04263a7/

---

# 📜 License

This project is developed for educational purposes only.

It is not intended to replace professional medical diagnosis or treatment.

---

<div align="center">

### ⭐ If you found this project helpful, please consider giving it a Star!

Made with ❤️ by **Manukonda Sridhar**

</div>
