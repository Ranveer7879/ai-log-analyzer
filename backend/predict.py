import joblib
import pandas as pd

MODEL_PATH = "model/isolation_forest.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


def predict(cpu, ram, disk):

    model = load_model()

    data = pd.DataFrame(
        [[cpu, ram, disk]],
        columns=["cpu", "ram", "disk"]
    )

    prediction = model.predict(data)[0]

    if prediction == -1:
        return "ANOMALY"

    return "NORMAL"


if __name__ == "__main__":

    print("Normal test:", predict(50, 40, 30))

    print("High usage test:", predict(95, 95, 90))