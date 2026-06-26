import sqlite3


def create_database():

    conn = sqlite3.connect("patient_history.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            patient_name TEXT,

            age INTEGER,

            gender TEXT,

            symptoms TEXT,

            predicted_disease TEXT,

            confidence REAL,

            prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()