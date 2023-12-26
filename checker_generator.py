import re
import random
import string

min_password_length = 8
required_strength_score = 5

def contains_uppercase(password):
    return re.search(r"[A-Z]", password) is not None

def contains_lowercase(password):
    return re.search(r"[a-z]", password) is not None

def contains_special_char(password):
    return re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~`]", password) is not None

def is_eight_chars_long(password):
    return len(password) >= min_password_length

def is_strong_password(password):
    criteria = [contains_uppercase, contains_lowercase, contains_special_char, is_eight_chars_long]
    strength_score = sum(criteria_func(password) for criteria_func in criteria)
    return strength_score >= required_strength_score

def generate_strong_pwd(length:int):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    password = input("Enter your password: ")
    if is_strong_password(password):
        print("Strong password! Good job!")
    else:
        print("Weak password. Choose a stronger one.")
        suggestion = generate_strong_pwd(12)
        print(f"Suggested strong password: {suggestion}")

if __name__ == "__main__":
    main()
