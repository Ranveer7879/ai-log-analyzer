# AI Log Analyzer

AI Log Analyzer is a Machine Learning based application that analyzes
server logs and detects unusual or anomalous behavior.

## Features

- CSV log analysis
- CPU usage analysis
- RAM usage analysis
- Log message analysis using TF-IDF
- Anomaly detection using Isolation Forest
- Severity detection
- REST API
- No OpenAI API required

## Technologies

- Python
- Flask
- Pandas
- Scikit-learn
- SciPy
- TF-IDF
- Isolation Forest

## Project Structure

ai-log-analyzer/
│
├── data/
│   └── logs.csv
│
├── train.py
├── app.py
├── requirements.txt
└── README.md

## Installation

Clone the project and open the project folder.

Create virtual environment:

python -m venv venv

Activate virtual environment on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Run the Application

python app.py

The application will start on:

http://127.0.0.1:5000

## API

### Home

GET /

Returns the application status.

### Analyze Logs

POST /analyze

Upload a CSV file for AI-based log analysis.

Required CSV columns:

- timestamp
- level
- message
- cpu
- ram

## Example

Input:

timestamp,level,message,cpu,ram

2026-09-01 10:00:00,INFO,Server started,30,40

2026-09-01 10:02:00,WARNING,High CPU usage,91,70

2026-09-01 10:03:00,ERROR,Database connection failed,95,85

Output:

NORMAL
WARNING
CRITICAL

## Machine Learning

The project uses Isolation Forest for anomaly detection.

TF-IDF is used to convert log messages into numerical features.

CPU and RAM usage are combined with text features to detect
unusual log patterns.

## OpenAI

This project does not use OpenAI or any external Generative AI API.

The anomaly detection is performed using a local Machine Learning model.

## Future Improvements

- Web dashboard
- Real-time log monitoring
- Docker deployment
- AWS deployment
- Email alerts
- Database integration
- Automatic log file monitoring