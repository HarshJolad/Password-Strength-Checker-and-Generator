import re
import random
import string

def strong_pwd(password):
    # Define the criteria for a strong password using regular expressions
    lowercase = re.compile(r'[a-z]')
    uppercase = re.compile(r'[A-Z]')
    digit = re.compile(r'\d')
    special_char = re.compile(r'[!@#$%^&*()_+{}\[\]:;<>,.?~`]')
    eight_chars = re.compile(r'^.{8,}$')

    # Check each criteria and assign a score for each fulfilled condition
    strength_score = 0
    if lowercase.search(password):
        strength_score += 1
    if uppercase.search(password):
        strength_score += 1
    if digit.search(password):
        strength_score += 1
    if special_char.search(password):
        strength_score += 1
    if eight_chars.search(password):
        strength_score += 1

    return strength_score >= 5

def generate_strong_pwd():
    # Generate a random strong password of 12 characters
    length = 12
    characters = string.ascii_letters + string.digits 
    strong_password = ''.join(random.choice(characters) for _ in range(length))
    return strong_password

def main():
    password = input("Enter your password: ")
    if strong_pwd(password):
        print("Strong password! Good job!")
    else:
        print("Weak password. Choose a stronger one.")
        suggestion = generate_strong_pwd()
        print(f"Suggested strong password: {suggestion}")

if __name__ == "__main__":
    main()
