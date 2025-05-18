students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    grade = input("Enter grade: ")
    student = {
        'name': name,
        'roll_no': roll_no,
        'grade': grade
    }
    students.append(student)
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("\n--- Student List ---")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Roll No: {student['roll_no']}, Grade: {student['grade']}")
    print()

def search_student():
    roll_no = input("Enter roll number to search: ")
    for student in students:
        if student['roll_no'] == roll_no:
            print(f"🎯 Found: Name: {student['name']}, Roll No: {student['roll_no']}, Grade: {student['grade']}\n")
            return
    print("❌ Student not found.\n")

def delete_student():
    roll_no = input("Enter roll number to delete: ")
    for student in students:
        if student['roll_no'] == roll_no:
            students.remove(student)
            print("🗑️ Student record deleted.\n")
            return
    print("❌ Student not found.\n")

def main():
    while True:
        print("📚 Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()