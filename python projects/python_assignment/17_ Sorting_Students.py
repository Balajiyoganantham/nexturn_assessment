# Exercise 17: Sorting Students by Marks
# Given a list of tuples where each tuple contains a student's name and their mark, write a program that sorts the list of students by their marks using a lambda 
def sort_students_by_marks(students):
    # Sorting the list of tuples by marks (second element in each tuple)
    sorted_students = sorted(students, key=lambda student: student[1])
    return sorted_students

# Example usage
if __name__ == "__main__":
    students = [
        ("John", 85),
        ("Alice", 78),
        ("Bob", 92),
        ("Daisy", 66),
        ("Charlie", 74)
    ]

    sorted_students = sort_students_by_marks(students)
    print("Students sorted by marks:")
    for student in sorted_students:
        print(f"{student[0]}: {student[1]}")
