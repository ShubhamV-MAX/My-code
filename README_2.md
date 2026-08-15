# 🛡️ Password Strength Analyzer

## Overview
This Python script is a lightweight **CLI (Command Line Interface)** tool designed to evaluate the strength and complexity of a password. It provides a foundational look into **InfoSec (Information Security)** principles, specifically focusing on password entropy, character diversity, and brute-force resistance. 

## ⚙️ Features
*   **Continuous Execution (REPL):** Utilizes a continuous `while` loop allowing the user to test multiple passwords consecutively without restarting the script.
*   **Comprehensive Character Checking:** Validates the presence of multiple character sets using Python's built-in string methods.
*   **Security Penalties:** Identifies and penalizes the inclusion of spaces, which can sometimes lead to parsing errors or indicate weak passphrase structures depending on the hashing backend.

## 📊 Evaluation Metrics & Rating System

| Criteria | Script Condition | Rating Impact | Technical Reasoning & Security Relevance |
| :--- | :--- | :--- | :--- |
| **Length** | `>= 8 Characters` | `+1` | Increases mathematical entropy, making automated brute-force attacks computationally expensive. |
| **Uppercase Letters** | `A-Z` (e.g., `.isupper()`) | `+1` | Expands the potential character pool by 26 characters. |
| **Lowercase Letters** | `a-z` (e.g., `.islower()`) | `+1` | Expands the potential character pool by 26 characters. |
| **Digits / Decimals** | `0-9` (e.g., `.isdecimal()`) | `+1` | Adds numeric variance, disrupting basic dictionary-based attacks. |
| **Special Characters** | `!@#$...` (`string.punctuation`) | `+1` | Utilizes standard punctuation to heavily diversify the required brute-force character space. |
| **Spaces** | `" "` (e.g., `.isspace()`) | `-1` | Penalizes spaces, which can occasionally cause vulnerabilities or input sanitation issues in legacy systems. |

## 📚 Technical Glossary & Short Forms
*   **CLI (Command Line Interface):** A text-based user interface used to view and manage computer files and execute scripts.
*   **InfoSec (Information Security):** The practice of protecting digital and physical information from unauthorized access, disclosure, or destruction.
*   **REPL (Read-Eval-Print Loop):** An interactive programming environment that takes user inputs, evaluates the logic, prints the result, and loops back to the start (implemented via the `while i == "y"` loop).
*   **ASCII (American Standard Code for Information Interchange):** A foundational character encoding standard for electronic communication. The script's `string.punctuation` module relies on these standardized symbol codes.
*   **Brute-Force Attack:** A cryptographic attack vector where an adversary submits numerous password combinations with the hope of eventually guessing correctly. 
*   **Entropy:** In cyber security, it refers to the randomness or unpredictability of data. Higher password entropy means it is statistically much harder to crack.

## 🚀 How to Run
1.  Ensure you have **Python 3.x** installed on your local environment.
2.  Save the provided script to a file named `password_analyzer.py`.
3.  Open your terminal or command prompt.
4.  Navigate to the directory containing the file.
5.  Execute the script using the command: `python password_analyzer.py`
6.  Follow the interactive on-screen prompts to evaluate your passwords.
