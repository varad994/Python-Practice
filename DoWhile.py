
# Program to repeatedly ask for a password until correct (do-while loop equivalent)
while True:
    password = input("Enter the password: ")
    if password == "secret":
        print("Access granted!")
        break
    print("Incorrect password, try again.")
