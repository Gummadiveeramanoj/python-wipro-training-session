# smart_university_full.py
import json
import csv
from abc import ABC, abstractmethod

# ================= DECORATORS =================
def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper

# ================= DESCRIPTORS =================
class MarksDescriptor:
    def __get__(self, instance, owner):
        return instance._marks

    def __set__(self, instance, value):
        for m in value:
            if m < 0 or m > 100:
                raise ValueError("Marks should be between 0 and 100")
        instance._marks = value

class SalaryDescriptor:
    def __get__(self, instance, owner):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, instance, value):
        instance._salary = value

# ================= ABSTRACT CLASS =================
class Person(ABC):
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

# ================= STUDENT CLASS =================
class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def get_details(self):
        print("\nStudent Details")
        print("--------------------------------")
        print("Name      :", self.name)
        print("Role      : Student")
        print("Department:", self.department)

    @log_execution
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"

        print("\nStudent Performance Report")
        print("--------------------------------")
        print("Student Name :", self.name)
        print("Marks        :", self.marks)
        print("Average      :", round(avg, 1))
        print("Grade        :", grade)

        return avg, grade

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)

# ================= FACULTY CLASS =================
class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        print("\nFaculty Details")
        print("--------------------------------")
        print("Name      :", self.name)
        print("Role      : Faculty")
        print("Department:", self.department)

# ================= COURSE CLASS =================
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits

# ================= UNIVERSITY SYSTEM =================
class UniversitySystem:
    def __init__(self):
        self.students = {}
        self.faculty = {}
        self.courses = {}

    def add_student(self, student):
        if student.pid in self.students:
            raise ValueError("Student ID already exists")
        self.students[student.pid] = student

    def add_faculty(self, faculty):
        self.faculty[faculty.pid] = faculty

    def add_course(self, course):
        self.courses[course.code] = course

    def enroll_student(self, sid, course_code):
        self.students[sid].courses.append(self.courses[course_code])

    def generate_csv(self):
        with open("students_report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Department", "Average", "Grade"])

            for s in self.students.values():
                avg, grade = s.calculate_performance()
                writer.writerow([s.pid, s.name, s.department, round(avg,1), grade])

        print("\nCSV Report Generated: students_report.csv")

# ================= MAIN EXECUTION =================
if __name__ == "__main__":
    uni = UniversitySystem()

    try:
        # -------- STUDENTS --------
        s1 = Student("S101", "Manoj", "Computer Science", 4, [78, 85, 90, 88, 92])
        s2 = Student("S102", "Rahul", "Computer Science", 4, [72, 75, 70, 74, 76])
        s3 = Student("S103", "Sandya", "Information Technology", 3, [88, 90, 92, 85, 87])
        s4 = Student("S104", "Supriya", "Information Technology", 3, [80, 82, 78, 81, 79])
        s5 = Student("S105", "Harsitha", "Electronics", 5, [91, 93, 89, 90, 92])

        uni.add_student(s1)
        uni.add_student(s2)
        uni.add_student(s3)
        uni.add_student(s4)
        uni.add_student(s5)

        # -------- FACULTY --------
        f1 = Faculty("F201", "Sow", "Computer Science", 85000)
        uni.add_faculty(f1)

        # -------- COURSES --------
        c1 = Course("CS401", "Data Structures", 4, f1)
        c2 = Course("CS402", "Algorithms", 3, f1)

        uni.add_course(c1)
        uni.add_course(c2)

        # -------- ENROLLMENT --------
        uni.enroll_student("S101", "CS401")
        uni.enroll_student("S102", "CS401")
        uni.enroll_student("S103", "CS402")

        # -------- OUTPUT DEMO --------
        s1.get_details()
        f1.get_details()

        print("\nCompare Two Students (> operator)")
        print("--------------------------------")
        print("Manoj > Rahul :", s1 > s2)

        print("\nMerge Course Credits (+ operator)")
        print("Total Credits After Merge :", c1 + c2)

        uni.generate_csv()

    except Exception as e:
        print("Error:", e)

    print("\nThank you for using Smart University Management System")

