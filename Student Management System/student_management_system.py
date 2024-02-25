import re

class Student:
    def __init__(self, name, roll_number, grade):
        self.__name = name
        self.__roll_number = roll_number
        self.__grade = grade

    def get_name(self):
        return self.__name

    def get_roll_number(self):
        return self.__roll_number

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if isinstance(grade, int) and 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid input. Enter a score from 0 to 100")

    def __str__(self):
        return f"Name: {self.__name}, Roll Number: {self.__roll_number}, Grade: {self.__grade}"
    

class StudentManagementSystem:
    def __init__(self):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def list_students(self):
        for student in self.__students:
            print(student)

    def search_student(self, roll_number):
        for student in self.__students:
            if student.get_roll_number() == roll_number:
                print(student)
                return
        print("Not found")

    def update_student_grade(self, roll_number, grade):
        for student in self.__students:
            if student.get_roll_number() == roll_number:
                student.set_grade(grade)
                print("The score is updated")
                return
        print("Not found")
    
class Main:
    def __init__(self):
        self.__student_management_system = StudentManagementSystem()

    def run(self):
        while True:
            print("\nStudent Management System")
            print("1. Add a new student")
            print("2. View all students")
            print("3. Search by number")
            print("4. Update score")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter name: ")
                roll_number = int(input("Enter the number: "))
                grade = int(input("Enter the score: "))
                student = Student(name, roll_number, grade)
                self.__student_management_system.add_student(student)
            elif choice == 2:
                self.__student_management_system.list_students()
            elif choice == 3:
                roll_number = int(input("Enter the number: "))
                self.__student_management_system.search_student(roll_number)
            elif choice == 4:
                roll_number = int(input("Enter the number: "))
                grade = int(input("Enter the score: "))
                self.__student_management_system.update_student_grade(roll_number, grade)
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main = Main()
    main.run()