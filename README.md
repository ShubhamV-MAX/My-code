# Armstrong Number Checker

## Overview
This Python script determines whether a given integer is an Armstrong number. An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits, each raised to the power of the number of digits.

## Technical Explanation & Variables
Here is a detailed breakdown of the variables and technical abbreviations used in the script:
*   **`no` (Number)**: The integer input provided by the user to be checked.
*   **`temp` (Temporary Variable)**: Stores a reference to the original number, as the variable `no` is manipulated and reduced to `0` during the calculation.
*   **`l` (Length)**: The total number of digits in the given number. It serves as the mathematical exponent for the calculation.
*   **`iteration`**: A `range` object used to iterate through the digits of the number based on its length.
*   **`arm` (Armstrong Accumulator)**: The variable used to store the initial sum (`0`) and accumulate the final calculated value.
*   **`r` (Remainder/Digit)**: The single digit extracted from the number during each iteration. Calculated using the modulo operator (`% 10`), it isolates digits starting from the least significant digit (ls) to the most significant digit (ms).

## How It Works
*   The script prompts the user to input a number.
*   It calculates the length of the string representation of the number to determine the correct exponent.
*   It enters a `for` loop, isolating each digit using the modulo operator (`%`), raising it to the power of the length (`**`), and adding it to the `arm` sum.
*   The floor division operator (`//`) is used to truncate the last digit from `no` before the next iteration.
*   It compares the original `temp` number with the calculated `arm` sum to determine the result.
*   The script runs inside a `while` loop, allowing the user to retry or exit via an interactive prompt.

## Security & Robustness Note
As a best practice in software development and secure coding, it is highly recommended to implement robust input validation. Currently, the script uses `int(input(...))`. If a user enters non-numeric data (such as alphabetical characters or symbols), the script will throw a `ValueError` and crash. Implementing a `try...except` block would safely catch invalid or malicious inputs, handle the exception gracefully, and prevent unexpected termination.
