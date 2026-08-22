# 🛡️ Password Strength Analyzer

## Overview
This Python script is a lightweight **CLI (Command Line Interface)** tool designed to evaluate the strength and complexity of a password. It provides a foundational look into **InfoSec (Information Security)** principles, specifically focusing on password entropy, character diversity, and brute-force resistance. 

## ⚙️ Features
*   **Continuous Execution (REPL):** Utilizes a continuous `while` loop allowing the user to test multiple passwords consecutively without restarting the script.
*   **Comprehensive Character Checking:** Validates the presence of multiple character sets using Python's built-in string methods.

## 📊 Evaluation Metrics & Rating System

| Criteria | Script Condition | Rating Impact | Technical Reasoning & Security Relevance |
| :--- | :--- | :--- | :--- |
| **Length** | `>= 8 Characters` | `+1` | Increases mathematical entropy, making automated brute-force attacks computationally expensive. |
| **Uppercase Letters** | `A-Z` (e.g., `.isupper()`) | `+1` | Expands the potential character pool by 26 characters. |
| **Lowercase Letters** | `a-z` (e.g., `.islower()`) | `+1` | Expands the potential character pool by 26 characters. |
| **Digits / Decimals** | `0-9` (e.g., `.isdecimal()`) | `+1` | Adds numeric variance, disrupting basic dictionary-based attacks. |
| **Special Characters** | `!@#$...` (`string.punctuation`) | `+1` | Utilizes standard punctuation to heavily diversify the required brute-force character space. |
| **Spaces** | `" "` (e.g., `.isspace()`) | `+1` | Penalizes spaces, which can occasionally cause vulnerabilities or input sanitation issues in legacy systems. |

## 🚀 How to Run
1.  Ensure you have **Python 3.x** installed on your local environment.
2.  Save the provided script to a file named `password_analyzer.py`.
3.  Open your terminal or command prompt.
4.  Navigate to the directory containing the file.
5.  Execute the script using the command: `python password_analyzer.py`
6.  Follow the interactive on-screen prompts to evaluate your passwords.
