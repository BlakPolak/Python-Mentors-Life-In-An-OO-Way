import csv
import random
from person import Person


class Mentor(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, energy_level, humanity_level):
        Person.__init__(self, first_name, last_name, year_of_birth, gender)
        self.nickname = Person.check_if_correct(nickname, str)
        self.energy_level = Person.check_if_correct(energy_level, str)
        self.humanity_level = Person.check_if_correct(humanity_level, str)


    def __str__(self):
        return self.first_name+" "+self.last_name

    @staticmethod
    def create_by_csv(filename="data/mentors.csv"):
        """Loading data from csv file"""
        list_of_mentors_object = []
        with open(filename) as file:
            file_reader = csv.reader(file)
            for data in file_reader:
                list_of_mentors_object.append(Mentor(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        return list_of_mentors_object

    def is_loving_gymnastic(self, mood_for_gymnastic):
        if random.randint(0, 10) < int(mood_for_gymnastic):
            return False
        return True


    def is_paying_attention(self, knowledge_desire):
        if random.randint(0, 10) < int(knowledge_desire):
            return False
        return True

    def do_gymnastics(self, mentor, students):
        print("Mentor "+mentor.first_name+" is starting proper gymnastics routine...")
        for student in students:
            if student.first_name[-1] == 'a':
                his_or_her = 'Her'
            else:
                his_or_her = 'His'
            if self.is_loving_gymnastic(student.mood_for_gymnastic):
                student.energy_level += 2
                print("Student "+student.first_name, student.last_name+ " enjoyed gymnastics and  gains some energy.\n"+
                                                                       str(his_or_her)+ " actual energy level is", student.energy_level, "\n")
            else:
                student.energy_level -= 2
                print("Student " + student.first_name, student.last_name + " hates gymnastics and loose some energy.\n"+
                                                                            str(his_or_her)+ " actual energy level is", student.energy_level, "\n")

    def give_motivational_speech(self, mentor, students):
        print("Mentor " + mentor.first_name + " gives great motivational speech ...\n")
        for student in students:
            if student.first_name[-1] == 'a':
                his_or_her = 'Her'
            else:
                his_or_her = 'His'
            if self.is_paying_attention(student.knowledge_desire):
                student.knowledge_level += 2
                mentor.humanity_level += 1
                print("Student " + student.first_name, student.last_name + " was paying attention and gains some knowledge.\n" +
                                                                           str(his_or_her) + " actual knowledge level is", student.knowledge_level, "\n")
            else:
                student.energy_level -= 2
                print("Student " + student.first_name, student.last_name + " wasn't paying attention and just loose some energy.\n" +
                                                                           str(his_or_her) + " actual energy level is", student.energy_level, "\n")


