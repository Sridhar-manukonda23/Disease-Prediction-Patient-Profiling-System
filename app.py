from flask import Flask, render_template, request, redirect, send_file, session
import joblib
import pandas as pd
import sqlite3
from pdf_generator import generate_pdf
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
app = Flask(__name__)
app.secret_key = "disease_prediction_secret_key"
model = joblib.load("disease_model.pkl")
encoder = joblib.load("symptom_encoder.pkl")


@app.route("/")
def home():
    return render_template(
        "index.html",
        symptoms=all_symptoms
    )


@app.route("/predict", methods=["POST"])
def predict():
    patient_name = request.form.get("patient_name")
    age = request.form.get("age")
    gender = request.form.get("gender")  
    selected_symptoms = [
        symptom.strip()
        for symptom in request.form.getlist("symptoms")
    ]
    if not selected_symptoms:
        return render_template(
            "index.html",
            symptoms=all_symptoms,
            error="Please select at least one symptom."
        )
    print("Selected Symptoms:", selected_symptoms)

    input_data = encoder.transform([selected_symptoms])

    print("Encoded Vector Shape:", input_data.shape)
    print("Non-zero Features:", input_data.sum())

    probabilities = model.predict_proba(input_data)[0]

    diseases = model.classes_

    results = list(zip(diseases, probabilities))

    results.sort(key=lambda x: x[1], reverse=True)

    print("Top 5 Predictions:", results[:5])

    top3 = results[:3]

    predicted_disease = top3[0][0]
    confidence = round(top3[0][1] * 100, 2)

    # Get Description
    description = description_df[
        description_df["Disease"] == predicted_disease
    ]["Description"].values

    if len(description) > 0:
        description = description[0]
    else:
        description = "Description not available."

    # Get Precautions
    # Get Precautions
    precautions = precaution_df[
        precaution_df["Disease"] == predicted_disease
    ]

    if len(precautions) > 0:
        precautions = precautions.iloc[0, 1:].dropna().tolist()
    else:
        precautions = []
    
    # Save patient record

    conn = sqlite3.connect("patient_history.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients
    (patient_name, age, gender, symptoms, predicted_disease, confidence)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (

        patient_name,
        age,
        gender,
        ", ".join(selected_symptoms),
        predicted_disease,
        confidence

    ))

    conn.commit()
    conn.close()
    session["report"] = {
    "patient_name": patient_name,
    "age": age,
    "gender": gender,
    "symptoms": ", ".join(selected_symptoms),
    "disease": predicted_disease,
    "confidence": confidence,
    "description": description,
    "precautions": precautions
    }
    
    return render_template(
        "result.html",
        disease=predicted_disease,
        confidence=confidence,
        description=description,
        precautions=precautions,
        predictions=top3
    )
df = pd.read_csv("dataset/dataset.csv")
description_df = pd.read_csv("dataset/symptom_Description.csv")
precaution_df = pd.read_csv("dataset/symptom_precaution.csv")

symptom_columns = [col for col in df.columns if "Symptom" in col]

all_symptoms = set()

for col in symptom_columns:
    for symptom in df[col].dropna():
        all_symptoms.add(str(symptom).strip())

all_symptoms = sorted(list(all_symptoms))

@app.route("/history")
def history():

    conn = sqlite3.connect("patient_history.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
        id,
        patient_name,
        age,
        gender,
        predicted_disease,
        confidence,
        prediction_date
        FROM patients
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    

    # Dashboard Statistics
    cursor.execute("SELECT COUNT(*) FROM patients")
    total_patients = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT predicted_disease) FROM patients")
    total_diseases = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM patients")
    total_predictions = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "history.html",
        records=records,
        total_patients=total_patients,
        total_diseases=total_diseases,
        total_predictions=total_predictions
    )

@app.route("/delete/<int:id>")
def delete_record(id):

    conn = sqlite3.connect("patient_history.db")

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/history")

@app.route("/download_report")
def download_report():

    report = session.get("report")

    if not report:
        return redirect("/")

    pdf = generate_pdf(report)

    return send_file(
        pdf,
        as_attachment=True,
        download_name="Disease_Prediction_Report.pdf",
        mimetype="application/pdf"
    )

@app.route("/loading")
def loading():
    return render_template("loading.html")
    
if __name__ == "__main__":
    app.run(debug=True)