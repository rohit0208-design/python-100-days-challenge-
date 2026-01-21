s = input("Enter username: ")
validate_string = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890@_"
if len(s) < 8:
    print("Invalid username: length should be at least 8")
else:
    # First character check
    if s[0].isupper() or s[0].islower():
        invalid = False

        for i in range(1, len(s)):
            if s[i] not in validate_string:
                print(f"Invalid username: invalid character '{s[i]}'")
                invalid = True
                break

        if not invalid:
            print("Username is valid ")
    else:
        print("Invalid username: first character must be a letter")
