import requests
import psutil
import socket
import time


# Backend API URL
SERVER_URL = "http://127.0.0.1:5000/api/metrics"


def collect_metrics():

    # CPU usage
    cpu = psutil.cpu_percent(interval=1)

    # RAM usage
    ram = psutil.virtual_memory().percent

    # Disk usage - Windows
    disk = psutil.disk_usage("C:\\").percent

    # Computer name
    machine = socket.gethostname()

    data = {
        "machine": machine,
        "cpu": cpu,
        "ram": ram,
        "disk": disk
    }

    return data


def send_data(data):

    try:

        response = requests.post(
            SERVER_URL,
            json=data,
            timeout=5
        )

        print("Data sent successfully")
        print(response.json())

    except requests.exceptions.RequestException as e:

        print("Backend connection error:", e)


def main():

    print("==============================")
    print(" AI Monitoring Agent Started")
    print("==============================")


    while True:

        # Collect computer data
        data = collect_metrics()

        print("------------------------------")
        print("Machine:", data["machine"])
        print("CPU:", data["cpu"], "%")
        print("RAM:", data["ram"], "%")
        print("Disk:", data["disk"], "%")

        # Send data to backend
        send_data(data)

        # Wait 5 seconds
        time.sleep(5)


if __name__ == "__main__":
    main()