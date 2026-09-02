from flask import Flask, request, jsonify,render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import IsolationForest
from scipy.sparse import hstack

app = Flask(__name__)


def analyze_logs(df):
    # Log message ko text feature mein convert karo
    messages = df["message"].fillna("")

    vectorizer = TfidfVectorizer()
    text_features = vectorizer.fit_transform(messages)

    # CPU + RAM features
    numeric_features = df[["cpu", "ram"]].values

    # Text + CPU + RAM combine
    features = hstack([
        text_features,
        numeric_features
    ])

    # AI model
    model = IsolationForest(
        contamination=0.2,
        random_state=42
    )

    model.fit(features)

    # Prediction
    df["prediction"] = model.predict(features)

    # Anomaly score
    df["anomaly_score"] = model.decision_function(features)

    # Severity
    def get_severity(row):
        if row["prediction"] == -1:
            if row["cpu"] >= 90 or row["ram"] >= 90:
                return "CRITICAL"
            return "WARNING"

        return "NORMAL"

    df["severity"] = df.apply(get_severity, axis=1)

    # Response data
    results = []

    for _, row in df.iterrows():
        results.append({
            "timestamp": str(row["timestamp"]),
            "level": str(row["level"]),
            "message": str(row["message"]),
            "cpu": float(row["cpu"]),
            "ram": float(row["ram"]),
            "severity": row["severity"],
            "anomaly_score": round(float(row["anomaly_score"]), 4)
        })

    return results


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "file" not in request.files:
        return jsonify({
            "error": "Please upload a CSV file"
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "error": "No file selected"
        }), 400

    try:
        df = pd.read_csv(file)

        required_columns = [
            "timestamp",
            "level",
            "message",
            "cpu",
            "ram"
        ]

        missing_columns = [
            column for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:
            return jsonify({
                "error": "Missing columns",
                "columns": missing_columns
            }), 400

        results = analyze_logs(df)

        return jsonify({
            "total_logs": len(results),
            "results": results
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)