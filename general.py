import csv

def parse_student_row(row):
    return Student(
        name=row["m_name"],
        surname=row["m_surname"],
        email=row["m_email"],
        birth_year=int(row["m_birth_year"]),
        birth_month=int(row["m_birth_month"]),
        birth_day=int(row["m_birth_day"]),
        group=row["m_group"],
        rating=float(row["m_rating"]),
        phone_number=row["m_phone_number"]
    )

def load_students(filename):
    students = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = parse_student_row(row)
            students.append(student)
    return students

class Student:
    def __init__(self, name, surname, email, birth_year, birth_month, birth_day, group, rating, phone_number):
        self.m_name = name
        self.m_surname = surname
        self.m_email = email
        self.m_birth_year = birth_year
        self.m_birth_month = birth_month
        self.m_birth_day = birth_day
        self.m_group = group
        self.m_rating = rating
        self.m_phone_number = phone_number
