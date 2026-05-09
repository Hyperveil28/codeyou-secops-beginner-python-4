# Week 4 Homework: Loops and Iteration

## Automating Repetition for Security Tasks

This project demonstrates how Python loops can automate repetitive cybersecurity tasks. The script loops through a list of IP addresses, classifies each address as **internal** or **external**, and prints a clear summary of the results.

In a real cybersecurity workflow, this same logic could be expanded to review firewall logs, SIEM alerts, authentication records, or network scan results.

---

## Learning Goals

- Practice using `for` and `while` loops.
- Use lists to store multiple IP addresses.
- Apply conditional logic to classify network data.
- Count internal and external IP addresses.
- Connect Python automation to practical security analysis.

---

## Project File

```text
ip_classifier.py
```

---

## What the Script Does

The script:

1. Stores several IP addresses in a list.
2. Loops through each IP address.
3. Checks whether the IP belongs to a private/internal range.
4. Prints whether each IP is internal or external.
5. Counts the total number of internal and external IP addresses.
6. Prints a final summary report.

---

## Internal IP Ranges Used

The script classifies the following private IP ranges as internal:

| Private Range | Description |
|---|---|
| `10.0.0.0 – 10.255.255.255` | Private Class A range |
| `172.16.0.0 – 172.31.255.255` | Private Class B range |
| `192.168.0.0 – 192.168.255.255` | Private Class C range |

Any address outside these ranges is classified as external.

---

## Example IP List

```python
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
```

---

## Example Output

```text
CyberVeil IP Classification Report
----------------------------------
192.168.1.10 is INTERNAL
10.0.0.25 is INTERNAL
172.16.5.4 is INTERNAL
8.8.8.8 is EXTERNAL
45.33.32.156 is EXTERNAL
172.20.10.2 is INTERNAL
192.168.0.55 is INTERNAL
1.1.1.1 is EXTERNAL
----------------------------------
Summary
Internal IPs: 5
External IPs: 3
Total IPs Checked: 8
```

---

## How to Run

1. Open the project folder in VS Code.
2. Make sure the Python file is named:

```text
ip_classifier.py
```

3. Open a terminal in the project folder.
4. Run the script:

```bash
python ip_classifier.py
```

or, depending on your system:

```bash
python3 ip_classifier.py
```

---

## Challenge Features

This project can also be expanded to include:

- User input with a `while` loop.
- Dynamic IP address entry.
- Counters for internal and external addresses.
- Error handling for invalid IP address formats.
- Reading IP addresses from a log file.

---

## Cybersecurity Relevance

Security analysts often need to process repeated data points such as IP addresses, failed login attempts, alert records, or firewall events. Loops allow Python to automate this repetitive review process instead of requiring manual inspection.

This assignment shows the foundation of a larger automation workflow: collect data, loop through each item, classify it, count the results, and generate a readable report.

---

## Reflection

This script demonstrates how loops improve efficiency in cybersecurity tasks. Instead of checking each IP address manually, the program repeats the same logic automatically for every address in the list. This makes the process faster, more consistent, and easier to scale for larger datasets.

---

## Author

Created for Week 4 Python homework: **Loops and Iteration – Automating Repetition for Security Tasks**.
