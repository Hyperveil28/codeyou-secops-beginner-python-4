# Week 4 Homework
# Loops and Iteration – Automating Repetition for Security Tasks
# File: loops_ips.py

"""
This script loops through IP addresses and classifies each one as internal or external.

It demonstrates:
- for loops
- while loops
- lists
- conditionals
- counters
- appending results into new lists
"""


def is_internal_ip(ip):
    """
    Determines whether an IP address is internal/private.

    Internal/private ranges checked:
    - 10.x.x.x
    - 192.168.x.x
    - 172.16.x.x through 172.31.x.x
    """

    if ip.startswith("10."):
        return True

    if ip.startswith("192.168."):
        return True

    if ip.startswith("172."):
        parts = ip.split(".")

        if len(parts) >= 2:
            second_octet = int(parts[1])

            if 16 <= second_octet <= 31:
                return True

    return False


# ------------------------------------------------------------
# Challenge 1 and Challenge 2
# Count internal vs external IPs and store results in new lists
# ------------------------------------------------------------

ip_addresses = [
    "192.168.1.10",
    "10.0.0.25",
    "172.16.5.4",
    "8.8.8.8",
    "45.33.32.156",
    "172.20.10.2",
    "192.168.0.55",
    "1.1.1.1"
]

internal_count = 0
external_count = 0

internal_ips = []
external_ips = []

print("CyberVeil IP Classification Report")
print("----------------------------------")

for ip in ip_addresses:
    if is_internal_ip(ip):
        print(f"{ip} is internal.")
        internal_count += 1
        internal_ips.append(ip)
    else:
        print(f"{ip} is external.")
        external_count += 1
        external_ips.append(ip)

print("----------------------------------")
print("Summary")
print(f"Internal: {internal_count}")
print(f"External: {external_count}")
print(f"Total IPs Checked: {len(ip_addresses)}")

print("\nInternal IP List:")
print(internal_ips)

print("\nExternal IP List:")
print(external_ips)


# ------------------------------------------------------------
# Challenge 3
# Looping from user input
# ------------------------------------------------------------

print("\nInteractive IP Classifier")
print("-------------------------")
print("Enter IP addresses one at a time.")
print("Type 'done' to finish.\n")

while True:
    user_ip = input("Enter an IP (or 'done' to finish): ")

    if user_ip.lower() == "done":
        print("Finished interactive classification.")
        break

    if is_internal_ip(user_ip):
        print(f"{user_ip} is internal.")
    else:
        print(f"{user_ip} is external.")
