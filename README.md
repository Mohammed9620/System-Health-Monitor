# 🖥️ System Health Monitor (SHM)

A professional Python-based monitoring tool designed to track system resources (CPU & RAM) and trigger automated email alerts when thresholds are exceeded.

## 🚀 Key Features
- **Real-time Monitoring**: Tracks hardware utilization using the `psutil` library.
- **Automated Alerting**: Sends instant email notifications via SMTP (Gmail) when critical limits are hit.
- **Incident Logging**: Records every alert with a precise timestamp in `alerts.log.txt` for future audit.
- **Clean Architecture**: Separates the monitoring logic from the notification service for better maintainability.

## 🛠️ Requirements
Ensure you have the `psutil` library installed:
```bash
pip install psutil

⚙️ Configuration
Open Email_send.py.

Update the From and To email addresses.

Provide your Google App Password in the server.login method (Never share your real password).

📂 File Structure
main.py: The main loop and resource analysis logic.

Email_send.py: Dedicated class for SMTP email dispatching.

alerts.log.txt: Automatically generated file containing the history of system warnings.
