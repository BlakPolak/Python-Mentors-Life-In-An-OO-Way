from mentor import Mentor
from student import Student


class CodecoolClass:

    def __init__(self, location, year, students):
        self.location = location
        self.year = year
        self.students = students

    @staticmethod
    def create_local_school():
        students = Student.create_by_csv("data/students.csv")
        #mentors = Mentor.create_by_csv()
        return students

    def find_student_by_full_name(self, full_name):
        name_list = full_name.split(" ")
        for student in self.students:
            if student.first_name == name_list[0]:
                if student.last_name == name_list[1]:
                    print(student.first_name, student.last_name + " found in our class.")
                    return student
        print(full_name + " student is not in our class.")
        return False
