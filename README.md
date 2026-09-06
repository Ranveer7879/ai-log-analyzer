Aur README ke **Problem → Solution** part mein simple language honi chahiye:

```markdown
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

