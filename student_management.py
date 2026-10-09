
import csv
import os

FILE_NAME = "students.csv"
HEADERS = ["ID", "Name", "Age", "Course", "Email"]


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)


# Function with parameters and return value
def calculate_total(a, b):
    return a + b


# Add Student
def add_student():
    try:
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Student Name: ").strip()
        age = int(input("Enter Student Age: "))
        course = input("Enter Course: ").strip()
        email = input("Enter Email: ").strip()

        if not student_id or not name or not course or not email:
            print("All fields are required!")
            return

        if age <= 0:
            print("Age must be greater than zero!")
            return

        students = read_students()

        if any(row[0] == student_id for row in students):
            print("Student ID already exists!")
            return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, age, course, email])

        print("Student added successfully!")

    except ValueError:
        print("Invalid age! Please enter a number.")
    except (OSError, csv.Error) as e:
        print("File error:", e)
    finally:
        print("Add Student operation completed.")


# Read all student records
def read_students():
    create_file()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)
        return [row for row in reader if len(row) == 5]


# View Students
def view_students():
    try:
        students = read_students()

        if not students:
            print("No student records found.")
            return

        print("\n--- Student Records ---")
        for row in students:
            print(
                f"ID: {row[0]} | Name: {row[1]} | "
                f"Age: {row[2]} | Course: {row[3]} | Email: {row[4]}"
            )

    except (OSError, csv.Error) as e:
        print("Unable to read student records:", e)


# Search Student
def search_student():
    try:
        search_id = input("Enter Student ID to search: ").strip()
        students = read_students()

        # Lambda function
        student = next(
            filter(lambda row: row[0] == search_id, students),
            None
        )

        if student:
            print("\nStudent Found!")
            print("ID:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])
            print("Email:", student[4])
        else:
            print("Student not found.")

    except (OSError, csv.Error) as e:
        print("Unable to search records:", e)


# Update Student
def update_student():
    try:
        search_id = input("Enter Student ID to update: ").strip()
        students = read_students()
        found = False

        for row in students:
            if row[0] == search_id:
                print("Leave a field blank to keep its current value.")

                name = input(f"New Name [{row[1]}]: ").strip()
                age = input(f"New Age [{row[2]}]: ").strip()
                course = input(f"New Course [{row[3]}]: ").strip()
                email = input(f"New Email [{row[4]}]: ").strip()

                if name:
                    row[1] = name

                if age:
                    new_age = int(age)
                    if new_age <= 0:
                        print("Age must be greater than zero!")
                        return
                    row[2] = str(new_age)

                if course:
                    row[3] = course

                if email:
                    row[4] = email

                found = True
                break

        if found:
            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(HEADERS)
                writer.writerows(students)

            print("Student updated successfully!")
        else:
            print("Student not found.")

    except ValueError:
        print("Invalid age! Please enter a valid number.")
    except (OSError, csv.Error) as e:
        print("Unable to update record:", e)


# Delete Student
def delete_student():
    try:
        search_id = input("Enter Student ID to delete: ").strip()
        students = read_students()

        remaining_students = [
            row for row in students if row[0] != search_id
        ]

        if len(remaining_students) == len(students):
            print("Student not found.")
            return

        confirm = input("Confirm deletion? (yes/no): ").strip().lower()

        if confirm != "yes":
            print("Deletion cancelled.")
            return

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
            writer.writerows(remaining_students)

        print("Student deleted successfully!")

    except (OSError, csv.Error) as e:
        print("Unable to delete record:", e)


# Main Menu
def main():
    create_file()

    while True:
        try:
            print("\n===== Student Record Management System =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

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
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice! Enter a number from 1 to 6.")

        except (KeyboardInterrupt, EOFError):
            print("\nProgram interrupted.")
            break
        finally:
            pass


if __name__ == "__main__":
    main()
