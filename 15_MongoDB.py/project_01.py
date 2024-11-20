import pymongo

# --------------------------Connect to MongoDB-------------------------------
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["college_db"]

# --------------------------Define collections--------------------------------
students_collection = db["students"]
courses_collection = db["courses"]
faculty_collection = db["faculty"]

# --------------------------Function to add a student--------------------------
def add_student():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    course = input("Enter course: ")
    student_data = {
        "name": name,
        "roll_number": roll_number,
        "course": course
    }
    students_collection.insert_one(student_data)
    print("Student added successfully!")

# --------------------------Function to view all students--------------------------
def view_students():
    for student in students_collection.find():
        print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Course: {student['course']}")

# --------------------------Function to search for a student-----------------------
def search_student():
    roll_number = input("Enter roll number to search: ")
    student = students_collection.find_one({"roll_number": roll_number})
    if student:
        print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Course: {student['course']}")
    else:
        print("Student not found.")

# --------------------------Similar functions for courses and faculty--------------------------

#-------------------------- Main menu--------------------------
while True:
    print("\n-----------------College Management System-----------------")
    print("1 for Add Student")
    print("2 for View Students")
    print("3 for Search Student")
    # ... (other options)
    print("0 for Exit")

    choice = input("Enter your choice (0,1,2,3): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    # ... (other options)
    elif choice == '0':
        break
    else:
        print("Invalid choice.")