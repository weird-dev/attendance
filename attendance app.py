# %%
import sqlite3

def create_table():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY, name TEXT, matric_number TEXT, department TEXT)''')
    conn.commit()
    conn.close()

def add_student(name, matric_number, department):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute('''INSERT INTO students (name, matric_number, department)
                 VALUES (?, ?, ?)''', (name, matric_number, department))
    conn.commit()
    conn.close()

def main():
    create_table()
    while True:
        print("\nWelcome to the Attendance System")
        print("1. Add Student")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            matric_number = input("Enter student's matric number: ")
            department = input("Enter student's department: ")
            add_student(name, matric_number, department)
            print("Student added successfully!")

        elif choice == '2':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



