import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import IsolationForest
from scipy.sparse import hstack


# Load logs
df = pd.read_csv("data/logs.csv")

# Text → numbers
messages = df["message"].fillna("")

vectorizer = TfidfVectorizer()
text_features = vectorizer.fit_transform(messages)

# CPU + RAM
numeric_features = df[["cpu", "ram"]].values

# Combine features
features = hstack([
    text_features,
    numeric_features
])

# AI model
model = IsolationForest(
    contamination=0.2,
    random_state=42
)

# Train
model.fit(features)

# Prediction
df["prediction"] = model.predict(features)

# Anomaly score
df["anomaly_score"] = model.decision_function(features)


# Severity function
def get_severity(row):

    if row["prediction"] == -1:

        if row["cpu"] >= 90 or row["ram"] >= 90:
            return "CRITICAL"

        return "WARNING"

    return "NORMAL"


df["severity"] = df.apply(get_severity, axis=1)


# Final output
print("\n========== AI LOG ANALYZER ==========\n")

for _, row in df.iterrows():

    print(f"Time     : {row['timestamp']}")
    print(f"Level    : {row['level']}")
    print(f"Message  : {row['message']}")
    print(f"CPU      : {row['cpu']}%")
    print(f"RAM      : {row['ram']}%")
    print(f"Severity : {row['severity']}")
    print(f"Score    : {row['anomaly_score']:.4f}")
    print("-" * 45)