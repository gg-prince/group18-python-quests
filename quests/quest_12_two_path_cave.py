SECRET_PASSWORD = "dragon123"

attempt = input("Enter the password: ")

if attempt == SECRET_PASSWORD:
    print("Access Granted. Welcome in!")
else:
    print("Access Denied. Turn back!")
