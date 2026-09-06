# 🤖 AI Server Monitoring & Anomaly Detection Platform

An AI-powered server monitoring platform that continuously monitors
CPU, RAM and Disk usage of servers and detects unusual system behavior
using Machine Learning.

The goal of this project is to build a real-world monitoring platform
for DevOps Engineers and System Administrators where multiple servers
can be monitored from a single centralized dashboard

# ❗ Problem Statement

When multiple servers are used in an organization, continuously
checking CPU, RAM and Disk usage manually is difficult.

A server may experience:

- High CPU usage
- Increasing RAM usage
- Low disk space
- Unusual resource consumption
- Performance degradation

Without centralized monitoring, administrators may not identify these
problems quickly.

# 💡 Proposed Solution

This project provides an AI-powered centralized server monitoring
system.

A lightweight monitoring agent runs on each server and automatically
collects system metrics.

The data is sent to a Flask backend, stored in MySQL and analyzed
using an Isolation Forest Machine Learning model.

The result is displayed on a centralized dashboard.

The system can also be extended to send alerts when an anomaly is
detected.

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend, Agent and AI |
| Flask | REST API / Backend |
| MySQL | Store monitoring data |
| Psutil | Collect CPU, RAM and Disk |
| Requests | Send agent data to backend |
| Pandas | Data processing |
| Scikit-learn | Machine Learning |
| Isolation Forest | Anomaly detection |
| Joblib | Save/load ML model |
| HTML | Dashboard structure |
| CSS | Dashboard design |
| JavaScript | Dashboard data and interaction |
| Git/GitHub | Version control |

