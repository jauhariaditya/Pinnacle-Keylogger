🔐 Python-Based Keylogger for Security Research
📌 Project Overview
This is a simple Python-based keylogger designed for educational and research purposes. The keylogger captures and logs all keystrokes made by a user and stores them in a text file (keylog.txt). It handles common and special keys like space, enter, and decimal for clear readability.

This project aims to help cybersecurity students and professionals understand how keyloggers work, how attackers might use them, and how defensive mechanisms can be developed to detect and prevent them.

🎯 Features
✅ Real-Time Keystroke Logging
Logs every keypress and appends it to a file.

✅ Handles Special Keys
Converts special keys like space, enter, and decimal for better readability.

✅ Lightweight and Simple
Written in Python using minimal dependencies.

✅ Security Research Focused
Meant for learning purposes such as malware analysis and improving defensive techniques.

🛠️ Technologies Used
Programming Language: Python
Libraries:
keyboard (for capturing key events)
datetime (optional, used here for timestamp reference)
⚙️ How It Works
The script starts by displaying a welcome message.
It then listens for keystrokes and logs them to a file called keylog.txt.
Special keys are processed for better readability (e.g., [ENTER],   for space).
The keylogger stops when the esc key is pressed.
🚀 Usage Instructions
⚠️ Note: Only run this script in a controlled environment (such as your lab or testing VM) and with proper authorization. This project is for educational purposes only.

Install the required library:
pip install keyboard
Run the script: python keylogger.py

Check the log file: The captured keystrokes will be saved in keylog.txt in the same directory.

⚠️ Disclaimer
This project is intended strictly for ethical, educational, and research purposes only. Do not use this tool for malicious or unauthorized activities. Always ensure you have proper consent when testing on a system.

🙌 Acknowledgment This project was developed as part of my internship at Pinnacle Labs during a security-focused task on understanding malware behavior
