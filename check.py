import re

def check_password_strength(password):
    strength = 0
    remarks = ""
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "Very Weak"
    elif strength == 2:
        remarks = "Weak"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 4:
        remarks = "Strong"
    elif strength == 5:
        remarks = "Very Strong"

    print(f"Password: {password}")
    print(f"Strength: {strength}/5")
    print(f"Remarks: {remarks}")

if __name__ == "__main__":
    password = input("Enter the password: ")
    check_password_strength(password```
if __name__ == "__main__":
    password = input("Enter the password: ")
    check_password_strength(password)
