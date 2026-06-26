import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("dataset/dataset.csv")

# Collect symptom columns
symptom_columns = [col for col in df.columns if "Symptom" in col]

# Convert symptoms into list
symptoms = []

for _, row in df.iterrows():
    symptom_list = []

    for col in symptom_columns:
        value = row[col]

        if pd.notna(value):
            symptom_list.append(str(value).strip())

    symptoms.append(symptom_list)

# Convert symptoms to binary features
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(symptoms)

# Target
y = df["Disease"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.4f}")

# Save model
joblib.dump(model, "disease_model.pkl")
joblib.dump(mlb, "symptom_encoder.pkl")

print("Model saved successfully!")