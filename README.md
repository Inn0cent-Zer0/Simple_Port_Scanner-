# Simple_Port_Scanner
🛰️ Interactive TCP Port Scanner – Terminal Edition  
A sleek, responsive (and slightly dramatic) terminal tool built using Python.  
Scan any target host's open TCP ports with optional custom ranges, hostname resolution, and real-time output.  
Minimalistic. Efficient. Kinda nosy.  
Made for hackers who ask nicely first 😌

✨ Written with midnight brain cells, old caffeine, and one bleeding socket by Vaish 💻🐍⚡

**📸 Terminal Preview**
---

Enter target hostname or IP address: google.com
Enter port range (default 1‑1023, e.g. 20‑80): 80-85

============================================================
 Scan target : 142.250.193.142  (resolved from 'google.com')
 Port range  : 80‑85
 Scan started: 2025-07-07 21:07:35
============================================================

 Port     80 is OPEN
 Port     85 is OPEN

============================================================
Scan finished at 2025-07-07 21:07:37
---

**💡 Features**
---
🔎 Scan any IP address or domain (it auto-resolves)  
🛠️ Optional port range input (defaults to 1–1023)  
⚙️ 1-second timeout per port, so it won’t hang forever  
📟 Real-time display of open ports  
🚫 Graceful exit on Ctrl+C or invalid input  
📄 Clean terminal layout with status banners  
🧼 Code wrapped in try/except and context managers for neatness
---
**🚀 Technologies Used  **
🐍 Python 3 – the beautiful beast behind it all  
🔌 `socket` – for TCP connection attempts  
🕰️ `datetime` – for timestamping your nerdy adventure  
🧠 `sys` – for input validation and clean exits  
---

**🕹️ How to Use**
---

1. Clone or download the repo  
2. Open your terminal and navigate to the folder  
3. Run:
 -python port_scanner.py Or use python3 if required.
 - Type in the target (IP or domain)
 - Optionally type a port range like 20-100
 - Watch it go 📡
 - See which ports are open like a nosy little hacker (with permission, of course)
 - Ctrl+C anytime to cancel without frying your terminal
---

**📂 Folder Structure**
---

port_scanner/
├── port_scanner.py   # Main scanner script
└── README.md         # You're reading it

**🧠 What I Learned**
This project helped reinforce:

📡 Socket programming and TCP connection logic
🛑 Handling user input and graceful program exits
⏲️ Timeout settings and exception catching
💻 Clean CLI formatting for a better user experience
🧼 Writing modular, readable Python scripts
🧠 And how to be nosy without jail time (legally 😇)
---
**💬 Feedback & Contributions**
---
Wanna add UDP support? Multi-thread it for speed? Add banner grabbing?
Let’s gooo. Fork it, star it ⭐, or drop a PR.
You can even just read it and nod sagely. That’s cool too.
---

☕ Made with one socket, two sighs, and three “what port was that again?”
Thanks for checking it out 💙
