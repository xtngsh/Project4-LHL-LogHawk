⚠️ Disclaimer:

This script is not intended for real-world security use and was created as part of the Lighthouse Labs Cybersecurity Bootcamp for educational purposes. Base64 is not encryption—if you use it to "secure" sensitive data, you’re doing it wrong.


# Project4-LHL-LogHawk
My Lighthouse Labs Project 4 - LogHawk Automation Tool
# 🛡️ LogHawkP4 - Automated Log Aggregation and Threat Detection

LogHawkP4 is a simple and effective tool designed to automate the process of monitoring system logs for key security indicators such as failed login attempts, critical system alerts, suspicious script executions, and related IP addresses.

---

## 📁 Step-by-Step Instructions

---

### 1️⃣ Run the Bash Script

The Bash script collects multiple logs and combines them into one file for analysis.

```bash
bash ./aggregateLogHawk.sh
 What it does:

Aggregates the following log files:

access.log

app.log

auth.log

system.log

Saves them into:

/home/student/Downloads/P4LogHawkLogs/Output/aggLog.log

