correct_password = "python123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Enter the password: ")
    attempts += 1

    if password == correct_password:
        print("Access granted!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) left.")
else:
    print("Access denied! Too many failed attempts. Account locked.")