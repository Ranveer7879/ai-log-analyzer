# 🤖 AI Server Monitoring & Anomaly Detection Platform

An AI-powered server monitoring platform that continuously monitors
CPU, RAM and Disk usage of servers and detects unusual system behavior
using Machine Learning.

The goal of this project is to build a real-world monitoring platform
for DevOps Engineers and System Administrators where multiple servers
can be monitored from a single centralized dashboard.

---

# 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Project Workflow](#-project-workflow)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Database Design](#-database-design)
- [Machine Learning](#-machine-learning)
- [Backend API](#-backend-api)
- [Monitoring Agent](#-monitoring-agent)
- [Dashboard](#-dashboard)
- [Local Setup](#-local-setup)
- [How to Start the Project](#-how-to-start-the-project)
- [Testing](#-testing)
- [Production Architecture](#-production-architecture)
- [Deployment](#-deployment)
- [Security](#-security)
- [Real-World Usage](#-real-world-usage)
- [Future Improvements](#-future-improvements)
- [Project Status](#-project-status)
- [Author](#-author)

---

# 🚀 Project Overview

Traditional server monitoring requires administrators to manually
check CPU, RAM, Disk and system performance.

This project automates the monitoring process.

A lightweight monitoring agent runs on the user's computer or server
and continuously collects system metrics.

The collected data is sent to a Flask REST API.

The backend stores the data in MySQL and uses an Isolation Forest
Machine Learning model to detect unusual server behavior.

The results are displayed on a centralized web dashboard.

---

# ❗ Problem Statement

When an organization has multiple servers, manually monitoring every
server becomes difficult.

Problems include:

- High CPU usage may go unnoticed.
- RAM usage can continuously increase.
- Disk space may become full.
- Unusual resource usage may indicate a problem.
- Administrators need to check multiple machines separately.
- Historical monitoring data is difficult to manage manually.

---

# 💡 Solution

The proposed system provides a centralized AI-powered monitoring
platform.

The system:

```text
Collect Server Metrics
        ↓
Send Data to Backend
        ↓
Store Data in MySQL
        ↓
Analyze Using AI
        ↓
Detect Anomaly
        ↓
Display on Dashboard
        ↓
Generate Alerts
