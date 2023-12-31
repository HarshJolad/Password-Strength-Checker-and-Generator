# Password Strength Checker and Generator

A basic **Python**-based password strength checker that evaluates the strength of a password based on specific criteria and provides suggestions for improving weak passwords. 

## Introduction
This password strength checker is a command-line tool written in Python. It allows users to input a password and evaluates its strength based on the following criteria:

- At least one lowercase letter (a-z)
- At least one uppercase letter (A-Z)
- At least one digit (0-9)
- At least one special character
- Minimum length of 8 characters

The password is then assigned a strength score based on how many of these criteria it meets. If the password does not meet the minimum criteria, the tool suggests a strong password for the user.

## Usage

1. Run the password strength checker by executing the following command:  
```
python3 checker_generator.py
```
2. Enter the password you want to check when prompted.
3. The tool will display the password's strength score and provide appropriate feedback, indicating whether it is strong or weak. If the password is weak, a strong password suggestion will be given.