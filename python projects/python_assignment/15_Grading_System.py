# Exercise 15: Grading System
# Write a user-defined function calculate_grade(marks) that takes a student's marks and returns their grade based on the following criteria:
# • Marks >= 90: Grade A
# • Marks >= 75: Grade B
# • Marks >= 50: Grade C
# • Marks < 50: Grade F
# crt + /
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'F'

# Example usage
if __name__ == "__main__":
    try:
        marks_input = float(input("Enter the student's marks: "))
        if 0 <= marks_input <= 100:
            grade = calculate_grade(marks_input)
            print(f"Marks: {marks_input}, Grade: {grade}")
        else:
            print("Please enter marks between 0 and 100.")
    except ValueError:
        print("Please enter a valid number for marks.")
