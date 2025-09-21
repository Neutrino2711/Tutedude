
def print_grades(grades):
    if not grades:
        print("No student grades available.")
    else:
        print("Student Grades:")
        for student, grade in grades.items():
            print(f"{student}: {grade}")

def main():
    grades = {}

    while True:
        print("\nOptions:")
        print("1. Add a new student and grade")
        print("2. Update an existing student's grade")
        print("3. Print all student grades")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            if name in grades:
                print(f"{name} already exists. Use option 2 to update the grade.")
            else:
                grades[name] = grade
                print(f"Added {name} with grade {grade}.")
        elif choice == '2':
            name = input("Enter student name to update: ")
            if name in grades:
                grade = input("Enter new grade: ")
                grades[name] = grade
                print(f"Updated {name}'s grade to {grade}.")
            else:
                print(f"{name} does not exist. Use option 1 to add the student.")
        elif choice == '3':
            print_grades(grades)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()