# RUNGTA INTERNATIONAL SKILLS UNIVERSITY
# SCHOOL OF COMPUTER SCIENCE AND ENGINEERING
# BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND ENGINEERING
#
# PROJECT TITLE : Student Record Management System
# PROJECT NUMBER: PS No. 14
#
# STUDENT DETAILS
# ------------------------------------------------------------
# Name : SHREJAL DEWANGAN
# ERP ID : RU-26-00749
# Section : BE-CSE-AIML-1-26-1-J
#
# PROJECT DESCRIPTION
# ------------------------------------------------------------
# Maintain student records (roll number, name, course, marks)
# with options to add, view, search, update and delete records.
#
# Python concepts: Lists, Tuples, Dictionaries, Functions,
# Loops, Conditions and CRUD operations.
# ============================================================


# Store each student as a dictionary inside a list.
# A tuple is used to represent the fields of a student record.
students = []


def add_student():
    """Add a new student after validating the details."""
    print("\n--- Add Student Record ---")

    roll_no = input("Enter roll number: ").strip()

    if not roll_no:
        print("Roll number cannot be empty.")
        return

    if search_record(roll_no, display=False) is not None:
        print(f"Roll number {roll_no} already exists.")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): ").strip())
    except ValueError:
        print("Marks must be between 0 and 100.")
        return

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    record = {
        "roll_no": roll_no,
        "name": name,
        "course": course,
        "marks": marks
    }

    # Tuple representation of the record, as required.
    student_tuple = (roll_no, name, course, marks)
    students.append(record)

    print(
        f"Record added: {student_tuple[0]} | {student_tuple[1]} | "
        f"{student_tuple[2]} | {format_marks(student_tuple[3])}"
    )


def view_students():
    """Display all student records in a neat table."""
    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    print("-" * 62)
    print(f"{'Roll No.':<12}{'Name':<20}{'Course':<18}{'Marks':>8}")
    print("-" * 62)

    for student in students:
        print(
            f"{student['roll_no']:<12}"
            f"{student['name']:<20}"
            f"{student['course']:<18}"
            f"{format_marks(student['marks']):>8}"
        )

    print("-" * 62)


def search_record(roll_no, display=True):
    """Find a student using the unique roll number."""
    for student in students:
        if student["roll_no"] == roll_no:
            if display:
                print(
                    f"{student['roll_no']} | {student['name']} | "
                    f"{student['course']} | {format_marks(student['marks'])}"
                )
            return student

    if display:
        print(f"Roll number {roll_no} not found.")
    return None


def search_student():
    """Ask for a roll number and display the matching record."""
    print("\n--- Search Student ---")
    roll_no = input("Enter roll number to search: ").strip()
    search_record(roll_no)


def update_student():
    """Update the marks of an existing student."""
    print("\n--- Update Student Marks ---")
    roll_no = input("Enter roll number to update: ").strip()
    student = search_record(roll_no, display=False)

    if student is None:
        print(f"Roll number {roll_no} not found.")
        return

    try:
        new_marks = float(input("Enter new marks (0-100): ").strip())
    except ValueError:
        print("Marks must be between 0 and 100.")
        return

    if not 0 <= new_marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    student["marks"] = new_marks
    print(f"Marks updated: {format_marks(new_marks)}")


def delete_student():
    """Delete a student record using the roll number."""
    print("\n--- Delete Student Record ---")
    roll_no = input("Enter roll number to delete: ").strip()

    for index, student in enumerate(students):
        if student["roll_no"] == roll_no:
            del students[index]
            print(f"Record deleted: {roll_no}")
            return

    print(f"Roll number {roll_no} not found.")


def format_marks(marks):
    """Display whole-number marks without a decimal point."""
    if float(marks).is_integer():
        return str(int(marks))
    return str(marks)


def display_menu():
    """Display the main menu."""
    print("\n========== STUDENT RECORD MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")
    print("======================================================")


def main():
    """Run the menu-driven student record management system."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

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
            print("Thank you for using Student Record Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()