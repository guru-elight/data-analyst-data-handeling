# Student Management System

students = []


def add_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["ID"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully.")


def view_students():
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 60)

    for student in students:
        print(f"ID     : {student['ID']}")
        print(f"Name   : {student['Name']}")
        print(f"Age    : {student['Age']}")
        print(f"Course : {student['Course']}")
        print(f"Marks  : {student['Marks']}")
        print("-" * 60)


def search_student():
    search_value = input("Enter Student ID or Name: ").lower()
    found = False

    for student in students:
        if (student["ID"].lower() == search_value or
                student["Name"].lower() == search_value):

            print("\nStudent Found")
            print(f"ID     : {student['ID']}")
            print(f"Name   : {student['Name']}")
            print(f"Age    : {student['Age']}")
            print(f"Course : {student['Course']}")
            print(f"Marks  : {student['Marks']}")
            found = True

    if not found:
        print("Student not found.")


def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["ID"] == student_id:
            student["Name"] = input("Enter New Name: ")
            student["Age"] = int(input("Enter New Age: "))
            student["Course"] = input("Enter New Course: ")
            student["Marks"] = float(input("Enter New Marks: "))

            print("Student details updated successfully.")
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using the Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


main()