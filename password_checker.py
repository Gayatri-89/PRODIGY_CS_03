import re

def check_password_strength(password):
    feedback = []
    strength = 0

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    return strength, feedback

# Main program loop
while True:
    user_password = input("Enter your password: ")
    strength, feedback = check_password_strength(user_password)

    if strength == 5:
        print("✅ Strong password. Well done!")
        break
    elif 3 <= strength < 5:
        print("⚠️ Moderate password. Suggestions: " + " ".join(feedback))
    else:
        print("❌ Weak password. Suggestions: " + " ".join(feedback))

    print("Please try again.\n")
