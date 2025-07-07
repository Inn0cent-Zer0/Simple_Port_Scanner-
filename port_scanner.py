# PART ONE – Imports
import socket           # Provides low-level networking interface
import sys              # Used to exit the script in case of errors or interruptions
from datetime import datetime  # To print scan timestamps

# PART TWO – Collect user input
# Prompt user to enter a target IP or hostname
target_raw = input("Enter target hostname or IP address: ").strip()
if not target_raw:
    print("No target given. Exiting.")
    sys.exit()

# Attempt to resolve the hostname to an IPv4 address
try:
    target = socket.gethostbyname(target_raw)
except socket.gaierror:
    print(f"Unable to resolve '{target_raw}'.")
    sys.exit()

# Prompt user for optional port range
port_range = input("Enter port range (default 1‑1023, e.g. 20‑80): ").strip()
if port_range and "-" in port_range:
    try:
        start_port, end_port = [int(p) for p in port_range.split("-", 1)]
        # Validate the port range
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        print("Invalid range. Using default 1‑1023.")
        start_port, end_port = 1, 1023
else:
    # Default port range
    start_port, end_port = 1, 1023

# PART THREE – Display scan header
print("=" * 60)
print(f" Scan target : {target}  (resolved from '{target_raw}')")
print(f" Port range  : {start_port}‑{end_port}")
print(f" Scan started: {datetime.now()}")
print("=" * 60)

# PART FOUR – Perform the scan
try:
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set timeout for connection attempt
            result = s.connect_ex((target, port))  # Attempt to connect
            if result == 0:
                print(f"Port {port:>5} is OPEN")
except KeyboardInterrupt:
    print("\nScan interrupted by user.")
    sys.exit()

# Scan complete
print("=" * 60)
print("Scan finished at", datetime.now())
