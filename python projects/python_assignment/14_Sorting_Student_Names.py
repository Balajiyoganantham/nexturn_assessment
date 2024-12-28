#Write a program that takes a list of student names and sorts them in alphabetical order using Python's built-in sorting functions. Additionally, find the longest name in the list.



def sort_student_names(names):
    if not names:
        print("No names provided.")
        return

    sorted_names = sorted(names)
    longest_name = max(names, key=len)

    print("Sorted Names:")
    for name in sorted_names:
        print(name)
    print(f"\nLongest name: {longest_name} (Length: {len(longest_name)})")

# Example usage
if __name__ == "__main__":
    # Taking input from the user as a comma-separated string
    input_names = input("Enter student names separated by commas: ")
    names = [name.strip() for name in input_names.split(",") if name.strip()]
    sort_student_names(names)
