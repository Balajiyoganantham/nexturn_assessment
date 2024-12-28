correct_password = "password123"
attempts = 0

while attempts < 3:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access Granted")
        break
    attempts += 1
else:
    print("Access Denied")
