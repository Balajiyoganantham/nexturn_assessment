age = int(input("Enter your age: "))
score = int(input("Enter your exam score: "))

if 18 <= age <= 25 and score >= 70:
    print("Admission Granted")
else:
    print("Admission Denied")
