import re                             # Import regular expressions for pattern matching
from collections import Counter       # Import Counter to count how many times items appear
import os                             # Import OS tools to create folders and work with file paths

# === Step 1: Read the log file ===
with open("/Users/briones/Desktop/Shared/aggLog.txt", "r") as file:
    log_data = file.readlines()       # Read all lines into a list so we can check each one

# === Step 2: Prepare counters for patterns and IPs ===
total_counts = Counter()              # To store total number of matches for each category
ip_failed = Counter()                 # To store how many times each IP caused failed password
ip_critical = Counter()               # To store IPs related to CRITICAL entries
ip_scripts = Counter()                # To store IPs that ran .sh scripts

# === Step 3: Pattern to find IPv4 addresses ===
ip_regex = r'(\d{1,3}(?:\.\d{1,3}){3})'  # This matches IPs like 192.168.1.1

# === Step 4: Go through each log line and look for matches ===
for line in log_data:
    ip_match = re.search(ip_regex, line)         # Try to find an IP address in the line
    ip = ip_match.group(1) if ip_match else "Unknown"  # Use the IP if found, otherwise use "Unknown"

    if "Failed password" in line:         # If line contains "Failed password"
        total_counts["Failed Passwords"] += 1   # Increase total failed password count
        ip_failed[ip] += 1                     # Increase this IP’s failed password count

    if re.search(r"\bCRITICAL\b", line):  # If line contains the word CRITICAL (case-sensitive)
        total_counts["CRITICAL Entries"] += 1   # Increase total CRITICAL count
        ip_critical[ip] += 1                   # Increase this IP’s CRITICAL count

    if re.search(r"\b\S+\.sh\b", line):    # If line contains something like "attack.sh"
        total_counts[".sh Script Executions"] += 1   # Increase total script count
        ip_scripts[ip] += 1                       # Increase this IP’s script execution count

# === Step 5: Create a folder to save results ===
output_dir = "log_analysis_output"        # Name of folder for the output
os.makedirs(output_dir, exist_ok=True)    # Create the folder (do nothing if it already exists)

# === Step 6: Write the results to a new file ===
output_path = os.path.join(output_dir, "/Users/briones/Desktop/Shared/Outputs/AnalysisOutput.txt")  # Full path for the report file
with open(output_path, "w") as out_file:   # Open file for writing
    # Write total pattern counts
    for key, value in total_counts.items():
        out_file.write(f"{key}: {value}\n")   # Write total count for each category
    out_file.write("\n")

    # Write failed password IP summary
    out_file.write("== Failed Passwords by IP ==\n")
    for ip, count in ip_failed.items():
        out_file.write(f"{ip}: {count}\n")     # Write each IP and how many failed attempts

    # Write CRITICAL IP summary
    out_file.write("\n== CRITICAL Entries by IP ==\n")
    for ip, count in ip_critical.items():
        out_file.write(f"{ip}: {count}\n")     # Write each IP with CRITICAL messages

    # Write .sh script IP summary
    out_file.write("\n== .sh Script Executions by IP ==\n")
    for ip, count in ip_scripts.items():
        out_file.write(f"{ip}: {count}\n")     # Write each IP that ran a .sh script

# === Step 7: Print message to screen ===
print(f"Analysis complete. Report saved to: {output_path}")   # Notify user where the output went

# === End of Script ===