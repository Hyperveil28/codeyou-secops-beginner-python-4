# Week 4 Homework
# Loops and Iteration – Automating Repetition for Security Tasks
# File: loops_ips_advanced.py

"""
Advanced version:
- Reads IP addresses from ips.txt
- Classifies each IP as internal or external
- Stores internal and external IPs in separate lists
- Writes internal IPs to internal_ips.txt
- Writes external IPs to external_ips.txt
"""


def is_internal_ip(ip):
    """
    Determines whether an IP address is internal/private.

    Internal/private ranges checked:
    - 10.x.x.x
    - 192.168.x.x
    - 172.16.x.x through 172.31.x.x
    """

    parts = ip.split(".")

    # Basic format check
    if len(parts) != 4:
        return False

    try:
        octets = [int(part) for part in parts]
    except ValueError:
        return False

    for octet in octets:
        if octet < 0 or octet > 255:
            return False

    first_octet = octets[0]
    second_octet = octets[1]

    if first_octet == 10:
        return True

    if first_octet == 192 and second_octet == 168:
        return True

    if first_octet == 172 and 16 <= second_octet <= 31:
        return True

    return False


input_file = "ips.txt"
internal_output_file = "internal_ips.txt"
external_output_file = "external_ips.txt"

internal_ips = []
external_ips = []

print("CyberVeil Advanced IP Classification Report")
print("-------------------------------------------")

try:
    with open(input_file, "r") as f:
        ip_addresses = f.read().splitlines()

    for ip in ip_addresses:
        ip = ip.strip()

        if ip == "":
            continue

        if is_internal_ip(ip):
            print(f"{ip} is internal.")
            internal_ips.append(ip)
        else:
            print(f"{ip} is external.")
            external_ips.append(ip)

    with open(internal_output_file, "w") as out:
        for ip in internal_ips:
            out.write(ip + "\n")

    with open(external_output_file, "w") as out:
        for ip in external_ips:
            out.write(ip + "\n")

    print("-------------------------------------------")
    print("Summary")
    print(f"Internal: {len(internal_ips)}")
    print(f"External: {len(external_ips)}")
    print(f"Total IPs Checked: {len(internal_ips) + len(external_ips)}")
    print()
    print(f"Internal IPs written to: {internal_output_file}")
    print(f"External IPs written to: {external_output_file}")

except FileNotFoundError:
    print(f"Error: Could not find {input_file}.")
    print("Create ips.txt in the same folder and add one IP address per line.")
