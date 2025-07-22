⚠️ Disclaimer:

This script is not intended for real-world security use and was created as part of the Lighthouse Labs Cybersecurity Bootcamp for educational purposes. Base64 is not encryption—if you use it to "secure" sensitive data, you’re doing it wrong.


# Project4-LHL-LogHawk
My Lighthouse Labs Project 4 - LogHawk Automation Tool
# 🛡️ LogHawkP4 - Automated Log Aggregation and Threat Detection

LogHawkP4 is a simple and effective tool designed to automate the process of monitoring system logs for key security indicators such as failed login attempts, critical system alerts, suspicious script executions, and related IP addresses.

---

🚀 Features
✅ Aggregates 4 logs (access.log, app.log, auth.log and system.log) into 1 file
✅ Run Python Code to analyze the final aggregate text file
✅ Cron job running in background to automate the log generation every 30 mins, everyday

🛠️ Usage

### 1️⃣ Run the Bash Script

The Bash script collects multiple logs and combines them into one file for analysis.

```bash
bash ./aggregateLogHawk.sh

### 2️⃣ Run the Python Script:
python3 loghawkP4.py

### 3️⃣ Python Output Results
After execution, the script creates a report file:

swift
Copy
Edit
/Users/briones/Desktop/Shared/Outputs/AnalysisOutput.txt

### 4️⃣ Automate with Cron Job
To automate both the Bash and Python scripts:

Add this line to your crontab:
bash
Copy
Edit
*/30 * * * * /home/student/Downloads/P4LogHawkLogs/aggregateLogHawk.sh
📆 This will:

Run the aggregation and analysis every 30 minutes, every day

Free up the analyst to focus on other security tasks

💡 To edit your crontab, run:

bash
Copy
Edit
crontab -e

📝 License
Use this script responsibly. If you get caught encoding your credentials in Base64, we take zero responsibility. 😆

P.S. If you see Base64 in a login token, ask yourself: What are they trying to hide? 😏
