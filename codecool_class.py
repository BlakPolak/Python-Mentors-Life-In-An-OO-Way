import random
from mentor import Mentor
from student import Student


class CodecoolClass:

    def __init__(self, location, year, students, mentors):
        self.location = location
        self.year = year
        self.students = students
        self.mentors = mentors

    @staticmethod
    def create_local_school():
        students = Student.create_by_csv("data/students.csv")
        mentors = Mentor.create_by_csv("data/mentors.csv")
        return students, mentors

    def find_student_by_full_name(self, full_name):
        name_list = full_name.split(" ")
        for student in self.students:
            if student.first_name == name_list[0]:
                if student.last_name == name_list[1]:
                    print(student.first_name, student.last_name + " found in our class.")
                    return student
        print(full_name + " student is not in our class.")
        return False

    def find_mentor_by_full_name(self, full_name):
        name_list = full_name.split(" ")
        for mentor in self.mentors:
            if mentor.first_name == name_list[0]:
                if mentor.last_name == name_list[1]:
                    print(mentor.first_name, mentor.last_name + " mentor found in our class.")
                    return mentor
        print(full_name + " mentor is not in our class.")
        return False


    def check_overall_energy(self):
        energy = 0
        for student in self.students:
            energy += int(student.energy_level)
        for mentor in self.mentors:
            energy += int(mentor.energy_level)
        print("Overall energy equals ", energy)


    def is_loving_gymnastic(self, mood_for_gymnastic):
        if random.randint(0, 10) < int(mood_for_gymnastic):
            return False
        return True


    def is_paying_attention(self, humanity_level):
        if random.randint(0, 10) < int(humanity_level):
            return False
        return True

    def do_gymnastics(self, mentor):
        print("Mentor "+mentor.first_name+" is starting proper gymnastics routine...")
        for student in self.students:
            if self.is_loving_gymnastic(student.mood_for_gymnastic):
                student.energy_level += 2
                print("Student "+student.first_name, student.last_name+" enjoyed gymnastics and  gains some energy. "
                                                                       "Hes actual energy level is", student.energy_level)
            else:
                student.energy_level -= 2
                print("Student " + student.first_name, student.last_name + " hates gymnastics and loose some energy. "
                                                                           "Hes actual energy level is", student.energy_level)

    def give_motivational_speech(self, mentor):
        print("Mentor " + mentor.first_name + " gives great motivational speech ...")
        for student in self.students:
            if self.is_paying_attention(student.knowledge_desire):
                student.knowledge_level += 2
                print("Student " + student.first_name, student.last_name + " was paying attention and gains some knowledge. "
                                                                           "Hes actual knowledge level is",
                                                                            student.knowledge_level)
            else:
                student.energy_level -= 2
                print("Student " + student.first_name, student.last_name + " wasn't paying attention and just loose some energy. "
                                                                           "Hes actual energy level is", student.energy_level)