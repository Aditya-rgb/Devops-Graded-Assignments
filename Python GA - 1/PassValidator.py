def check_password_strength(password):
    special_characters = set("!@#$%^&*()-+?_=,<>/")

    criteria = {
        "length": len(password) > 8,
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "digit": any(char.isdigit() for char in password),
        "special_character": any(char in special_characters for char in password)
    }

    messages = {
        "length": "at least 8 characters long",
        "uppercase": "at least one uppercase letter",
        "lowercase": "at least one lowercase letter",
        "digit": "at least one digit",
        "special_character": "at least one special character"
    }

    for criterion, met in criteria.items():
        if met:
            print(f"Meets the {messages[criterion]} criteria...")
        else:
            print(f"Does not meet the {messages[criterion]} criteria.")

password = input("Enter your password: ")
check_password_strength(password)

