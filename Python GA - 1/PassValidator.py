def guard_checker(password):
    # Define special characters that are commonly used in passwords
    special_characters = set("!@#$%^&*()-+?_=,<>/")
    
    # Define rules to check for password strength
    rules = {
        "length": len(password) >= 8,  # Check if password length is at least 8 characters
        "uppercase": any(char.isupper() for char in password),  # Check for at least one uppercase letter
        "lowercase": any(char.islower() for char in password),  # Check for at least one lowercase letter
        "digit": any(char.isdigit() for char in password),  # Check for at least one digit
        "special_criteria": any(char in special_characters for char in password)  # Check for at least one special character
    }

    # Messages to inform the user about each critieria that gets missed
    prompts = {
        "length": "at least 8 characters long.",
        "uppercase": "at least one character should be in upper-case.",
        "lowercase": "at least one character should be in lower-case.",
        "digit": "at least one character should be numeric.",
        "special_criteria": "at least one special character."
    }

    all_rules_met = True

    # Check if all criteria are met
    for specs, met in rules.items():
        if not met:
            all_rules_met = False

    # If any rule is not met, provide feedback to the user
    if not all_rules_met:
        print("Uh-Oh! Your password is as fragile as a spider's web. Strengthen it!")
        print("")
        print("Please find the feedback below for your password:")
        for specs, met in rules.items():
            if not met:
                print(f"\033[1mYour password should have {prompts[specs]}\033[0m")  # Print feedback in bold

        return False
    else:
        return True

# Main loop to repeatedly ask for a password until a strong one is provided
while True:
    password = input("Enter your pass guard: ")
    if guard_checker(password):
        print("Great! Your password is as solid as a rock. Rock on!")
        break
    else:
        print("")
        print("Enter a robust password this time :)")
