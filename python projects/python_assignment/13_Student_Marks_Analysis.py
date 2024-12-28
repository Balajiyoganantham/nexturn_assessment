#Exercise 13: Student Marks Analysis
#Write a Python program that takes a list of students' marks (as input) and uses built-in functions to calculate the highest, lowest, and average marks.
def student_marks_analysis(marks):
    if not marks:
        print("No marks provided.")
        return

    highest_mark = max(marks)
    lowest_mark = min(marks)
    average_mark = sum(marks) / len(marks)

    print(f"Highest mark: {highest_mark}")
    print(f"Lowest mark: {lowest_mark}")
    print(f"Average mark: {average_mark:.2f}")

# Example usage
if __name__ == "__main__":
    try:
        # Taking input from the user as a comma-separated string
        input_marks = input("Enter student marks separated by commas: ")
        marks = [float(mark.strip()) for mark in input_marks.split(",") if mark.strip().isdigit()]
        student_marks_analysis(marks)
    except ValueError:
        print("Please enter valid numeric marks separated by commas.")
