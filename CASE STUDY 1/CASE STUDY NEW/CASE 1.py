from abc import ABC, abstractmethod
import json
import csv

# ===================== DESCRIPTORS =====================

class MarksDescriptor:
    def __set__(self, obj, value):
        if any(m < 0 or m > 100 for m in value):
            raise ValueError("Marks must be between 0 and 100")
        obj._marks = value

    def __get__(self, obj, objtype=None):
        return obj._marks


class SalaryDescriptor:
    def __get__(self, obj, objtype=None):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, obj, value):
        obj._salary = value


# ===================== DECORATORS =====================

def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__} executed successfully")
        return result
    return wrapper


# ===================== ABSTRACT BASE CLASS =====================

class Person(ABC):
    def __init__(self, pid, name, dept):
        self.pid = pid
        self.name = name
        self.dept = dept

    @abstractmethod
    def get_details(self):
        pass


# ===================== STUDENT CLASS =====================

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, dept, sem, marks):
        super().__init__(sid, name, dept)
        self.sem = sem
        self.marks = marks
        self.courses = []

    def __del__(self):
        print(f"Student {self.name} object destroyed")

    def enroll(self, course):
        self.courses.append(course)

    def get_details(self):
        print("\nStudent Details")
        print("----------------------")
        print("Name :", self.name)
        print("Dept :", self.dept)
        print("Sem  :", self.sem)

    @log_execution
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 80 else "B"
        print("\nPerformance Report")
        print("----------------------")
        print("Average :", round(avg, 2))
        print("Grade   :", grade)
        return avg

    def __gt__(self, other):
        return self.calculate_performance() > other.calculate_performance()


# ===================== FACULTY CLASS =====================

class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, dept, salary):
        super().__init__(fid, name, dept)
        self.salary = salary

    def get_details(self):
        print("\nFaculty Details")
        print("----------------------")
        print("Name :", self.name)
        print("Dept :", self.dept)


# ===================== COURSE CLASS =====================

class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits


# ===================== ITERATOR & GENERATOR =====================

class CourseIterator:
    def __init__(self, courses):
        self.courses = courses
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.courses):
            raise StopIteration
        val = self.courses[self.index]
        self.index += 1
        return val


def student_generator(students):
    print("\nFetching Student Records...")
    for s in students:
        yield f"{s.pid} - {s.name}"


# ===================== FILE HANDLING =====================

def save_json(students):
    data = []
    for s in students:
        data.append({
            "id": s.pid,
            "name": s.name,
            "department": s.dept,
            "semester": s.sem,
            "marks": s.marks
        })

    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Data saved to students.json")


def generate_csv(students):
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Dept", "Average", "Grade"])

        for s in students:
            avg = sum(s.marks) / len(s.marks)
            grade = "A" if avg >= 80 else "B"
            writer.writerow([s.pid, s.name, s.dept, round(avg, 2), grade])

    print("CSV report generated")


# ===================== MAIN MENU =====================

students = []
faculty_list = []
courses = []

while True:
    print("""
SMART UNIVERSITY MANAGEMENT SYSTEM
1 Add Student
2 Add Faculty
3 Add Course
4 Enroll Student
5 Performance Student
6 Compare Students
7 Reports of Student
8 Exit
""")

    ch = input("Enter choice: ")

    try:
        if ch == "1":
            sid = input("ID: ")
            name = input("Name: ")
            dept = input("Dept: ")
            sem = int(input("Semester: "))
            marks = list(map(int, input("Marks: ").split()))

            students.append(Student(sid, name, dept, sem, marks))
            print("Student Added")

        elif ch == "2":
            fid = input("ID: ")
            name = input("Name: ")
            dept = input("Dept: ")
            sal = int(input("Salary: "))

            faculty_list.append(Faculty(fid, name, dept, sal))
            print("Faculty Added")

        elif ch == "3":
            code = input("Code: ")
            name = input("Name: ")
            cr = int(input("Credits: "))
            fid = input("Faculty ID: ")

            fac = next((f for f in faculty_list if f.pid == fid), None)
            if not fac:
                print("Faculty not found")
                continue

            courses.append(Course(code, name, cr, fac))
            print("Course Added")

        elif ch == "4":
            sid = input("Student ID: ")
            code = input("Course Code: ")

            s = next((x for x in students if x.pid == sid), None)
            c = next((x for x in courses if x.code == code), None)

            if s and c:
                s.enroll(c)
                print("Enrollment Successful")
            else:
                print("Invalid Student or Course")

        elif ch == "5":
            sid = input("Student ID: ")
            s = next(x for x in students if x.pid == sid)
            s.calculate_performance()

        elif ch == "6":
            if len(students) >= 2:
                print(students[0].name, ">", students[1].name, ":", students[0] > students[1])
            else:
                print("Need at least two students")

        elif ch == "7":
            save_json(students)
            generate_csv(students)
            for rec in student_generator(students):
                print(rec)

        elif ch == "8":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")

    except Exception as e:
        print("Error:", e)
