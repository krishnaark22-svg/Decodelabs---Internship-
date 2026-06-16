import re
import hmac

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        return "Weak (Too short)"

    # Lowercase
    if any(c.islower() for c in password):
        score += 1

    # Uppercase
    if any(c.isupper() for c in password):
        score += 1

    # Digits
    if any(c.isdigit() for c in password):
        score += 1

    # Symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength classification
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"


# Secure comparison example (timing attack prevention)
def secure_compare(a, b):
    return hmac.compare_digest(a, b)


if __name__ == "__main__":
    pwd = input("Enter password: ")
    print("Strength:", check_password_strength(pwd))
