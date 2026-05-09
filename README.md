# Week 4 Homework
# Loops and Iteration – Automating Repetition for Security Tasks
# Script: IP Address Classifier


def is_internal_ip(ip):
    """
    Determines whether an IP address belongs to a private/internal range.
    """

    if ip.startswith("10."):
        return True

    if ip.startswith("192.168."):
        return True

    # Check 172.16.0.0 through 172.31.255.255
    if ip.startswith("172."):
        parts = ip.split(".")

        if len(parts) == 4:
            second_octet = int(parts[1])

            if 16 <= second_octet <= 31:
                return True

    return False


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

print("CyberVeil IP Classification Report")
print("----------------------------------")

for ip in ip_addresses:
    if is_internal_ip(ip):
        print(f"{ip} is INTERNAL")
        internal_count += 1
    else:
        print(f"{ip} is EXTERNAL")
        external_count += 1

print("----------------------------------")
print("Summary")
print(f"Internal IPs: {internal_count}")
print(f"External IPs: {external_count}")
print(f"Total IPs Checked: {len(ip_addresses)}")
