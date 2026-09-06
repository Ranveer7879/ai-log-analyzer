import mysql.connector
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "ranveer@#123",
    "database": "ai_monitor"
}


def train_model():

    connection = mysql.connector.connect(**DB_CONFIG)

    query = """
        SELECT cpu, ram, disk
        FROM metrics
    """

    df = pd.read_sql(query, connection)

    connection.close()

    if len(df) < 15:
        print("Not enough data for training.")
        return

    X = df[["cpu", "ram", "disk"]]

    model = IsolationForest(
        contamination=0.10,
        random_state=42
    )

    model.fit(X)

    os.makedirs("model", exist_ok=True)

    joblib.dump(
        model,
        "model/isolation_forest.pkl"
    )

    print("Model trained successfully!")


if __name__ == "__main__":
    train_model()