from getpass import getpass

isLoggedIn = False
while isLoggedIn == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username == "Ven" and password == "akonalangsana123":
        print("Login successful! huwag kalimutan ang password mo.")
        isLoggedIn = True
    else:
        print("Invalid credentials. Please try again.")
        isLoggedIn = False