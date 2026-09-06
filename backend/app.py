from flask import Flask, jsonify, request
from database import get_connection
from predict import predict

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "AI Server Monitoring Backend Running"
    })


@app.route("/api/metrics", methods=["POST"])
def receive_metrics():

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "No data received"
        }), 400

    try:
        machine = data["machine"]
        cpu = float(data["cpu"])
        ram = float(data["ram"])
        disk = float(data["disk"])

        # AI Prediction
        prediction = predict(cpu, ram, disk)

        # Save metrics to MySQL
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO metrics
            (machine, cpu, ram, disk)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                machine,
                cpu,
                ram,
                disk
            )
        )

        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({
            "status": "success",
            "message": "Metrics saved successfully",
            "machine": machine,
            "cpu": cpu,
            "ram": ram,
            "disk": disk,
            "prediction": prediction
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route("/api/metrics", methods=["GET"])
def get_metrics():

    try:

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT *
            FROM metrics
            ORDER BY timestamp DESC
            LIMIT 50
        """

        cursor.execute(query)

        metrics = cursor.fetchall()

        cursor.close()
        connection.close()

        # AI prediction for dashboard
        for item in metrics:

            item["timestamp"] = str(item["timestamp"])

            item["prediction"] = predict(
                float(item["cpu"]),
                float(item["ram"]),
                float(item["disk"])
            )

        return jsonify({
            "status": "success",
            "metrics": metrics
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )