def checkPassword():
    maxAttempts = 5
    correctPassword = "12345" 

    for attempt in range(maxAttempts):
        password = input("Enter password: ")

        if password == correctPassword:
            print("Correct! Access granted.")
            return
        else:
            print(f"Wrong password. You have {maxAttempts - attempt - 1} attempts left.")

    print("Too many failed attempts. Try again later.")

checkPassword()