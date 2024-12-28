
#description add client to access the server running in the flask
import requests

# Define the base URL for the Flask server
BASE_URL = "http://127.0.0.1:5000"

# Function to add a new teacher with user-specified ID
def add_teacher(teacher_id, name, subject):
    url = f"{BASE_URL}/teachers"
    data = {
        "id": teacher_id,
        "name": name,
        "subject": subject
    }
    response = requests.post(url, json=data)
    
    if response.status_code == 201:
        print("Teacher added successfully:", response.json())
    else:
        print("Failed to add teacher:", response.text)

# Function to delete a teacher by ID
def delete_teacher(teacher_id):
    url = f"{BASE_URL}/teachers/{teacher_id}"
    response = requests.delete(url)
    
    if response.status_code == 200:
        print("Teacher deleted successfully:", response.json())
    else:
        print("Failed to delete teacher:", response.text)

# Function to view all teachers
def view_all_teachers():
    url = f"{BASE_URL}/teachers"
    response = requests.get(url)
    
    if response.status_code == 200:
        teachers = response.json()
        print("\n--- List of Teachers ---")
        if teachers:
            for teacher in teachers:
                print(f"ID: {teacher['id']}, Name: {teacher['name']}, Subject: {teacher['subject']}")
        else:
            print("No teachers found.")
    else:
        print("Failed to retrieve teachers:", response.text)

# Main function to handle user choices
def main():
    while True:
        print("\n--- Teacher Management ---")
        print("1. Add a new teacher")
        print("2. Delete a teacher by ID")
        print("3. View all teachers")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            teacher_id = input("Enter teacher's ID: ")
            if teacher_id.isdigit():
                name = input("Enter teacher's name: ")
                subject = input("Enter teacher's subject: ")
                add_teacher(int(teacher_id), name, subject)
            else:
                print("Invalid ID. Please enter a number.")
        
        elif choice == "2":
            teacher_id = input("Enter the teacher ID to delete: ")
            if teacher_id.isdigit():
                delete_teacher(int(teacher_id))
            else:
                print("Invalid ID. Please enter a number.")
        
        elif choice == "3":
            view_all_teachers()
        
        elif choice == "4":
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the client program
if __name__ == "__main__":
    main()
