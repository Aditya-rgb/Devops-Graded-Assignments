def guard_checker(password):
    special_characters = set("!@#$%^&*()-+?_=,<>/")


    rules = {

        "length" : len(password) >= 8,
        "uppercase" : any(char.isupper() for char in password),
        "lowercase" : any(char.islower() for char in password),
        "digit" : any(char.isdigit() for char in password),
        "special_criteria" : any(char in special_characters for char in password)
            }
    

    prompts = {
        "length" : "at least 8 characters long.",
        "uppercase" : "at least one character should be in upper-case.",
        "lowercase" : "at least one character should be in lower-case.",
        "digit" : "at least one character should be numeric.",
        "special_criteria" : "at least one special character."
    }

    all_rules_met = True

    for specs, met in rules.items() :
        if not met :
            all_rules_met = False

    if not all_rules_met:
        print ("Uh-Oh! Your password is as fragile as a spider's web. Strengthen it!")
        print("")
        print("Please find the feedback below for your password : ")
        for specs, met in rules.items() :
            if not met :
                 print(f"\033[1mYour password should have {prompts[specs]}\033[0m")
                

        return False

    else : 
        return True    
    

while True:
    password = input("Enter your pass guard: ")
    if guard_checker(password):
        print("Great! Your password is as solid as a rock. Rock on!")
        break
    else:
        print("")
        print("Enter a robust password this time :)")

