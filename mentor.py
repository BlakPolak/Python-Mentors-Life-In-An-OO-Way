import csv
import random
import time
import os
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
        if random.randint(0, 10) < mood_for_gymnastic:
            return False
        return True


    def is_paying_attention(self, knowledge_desire):
        if random.randint(0, 10) < knowledge_desire:
            return False
        return True

    def do_gymnastics(self, students):
        print("\033[1mMentor "+self.first_name+" is starting proper gymnastics routine...\033[0m\n")
        time.sleep(2)
        for student in students:
            if student.first_name[-1] == 'a':
                his_or_her = 'Her'
            else:
                his_or_her = 'His'
            if self.is_loving_gymnastic(student.mood_for_gymnastic):
                student.energy_level += 2
                self.humanity_level += 1
                print(self.first_name, self.last_name + " has " + str(self.humanity_level) + " humanity points now")
                print("\x1b[32mStudent "+student.first_name, student.last_name + " enjoyed gymnastics and  gains some energy.\x1b[0m\n"+
                      str(his_or_her) + " actual energy level is", student.energy_level, "\n")
                time.sleep(2)
            else:
                student.energy_level -= 2
                self.humanity_level -= 1
                print("\x1b[31mStudent " + student.first_name, student.last_name
                      + " hates gymnastics and loose some energy.\x1b[0m\n"+
                      str(his_or_her) + " actual energy level is", student.energy_level, "\n")
        time.sleep(2)
        os.system('clear')

    def give_motivational_speech(self, students):
        print("\033[1mMentor " + self.first_name + " gives great motivational speech ...\033[0m\n")
        time.sleep(2)
        for student in students:
            if student.first_name[-1] == 'a':
                his_or_her = 'Her'
            else:
                his_or_her = 'His'
            if self.is_paying_attention(student.knowledge_desire):
                student.knowledge_level += 2
                self.humanity_level += 1
                print(self.first_name, self.last_name + " has " + str(self.humanity_level) + " humanity points now")
                print("\x1b[32mStudent " + student.first_name, student.last_name +
                      " was paying attention and gains some knowledge.\x1b[0m\n" +
                      str(his_or_her) + " actual knowledge level is", student.knowledge_level, "\n")
                time.sleep(2)
            else:
                student.energy_level -= 2
                self.humanity_level -= 1
                print("\x1b[31mStudent " + student.first_name, student.last_name +
                      " wasn't paying attention and just loose some energy.\x1b[0m\n" +
                      str(his_or_her) + " actual energy level is", student.energy_level, "\n")
            time.sleep(2)
        os.system('clear')

    def give_private_mentoring(self, student):
        print("\033[1mMentor " + self.first_name + " gives private mentoring for ",
              student.first_name, student.last_name + "\033[0m\n")
        time.sleep(2)
        self.humanity_level += 1
        student.knowledge_level += 2
        print("\x1b[32mMentors humanity has increased.\n" + self.first_name,
              self.last_name + " has " + str(self.humanity_level) + " humanity points now.\x1b[0m")
        time.sleep(0.5)
        print(self.first_name, self.last_name + " has " + str(self.humanity_level) + " humanity points now")
        print("\x1b[32mStudent " + student.first_name, student.last_name + " begins to understand a lot more!\x1b[0m\n" +
              "Actual knowledge level is", student.knowledge_level, "\n")
        time.sleep(2)
        os.system('clear')

    def drink_coffee_with_student(self, student):
        print("\033[1mMentor " + self.first_name + " drinks coffee with ",
              student.first_name, student.last_name + "\033[0m\n")
        time.sleep(2)
        self.humanity_level += 1
        student.energy_level += 2
        print(self.first_name, self.last_name + " has " + str(self.humanity_level) + " humanity points now")
        time.sleep(0.5)
        print("\x1b[32mStudent " + student.first_name, student.last_name + " energy has increased!\x1b[0m\n" +
              "Actual energy level is", student.energy_level, "\n")
        time.sleep(2)
        os.system('clear')

    def do_coding_dojo(self, student1, student2):
        print("\033[1mMentor " + self.first_name + " do Coding Dojo for ", student1.first_name, student1.last_name,
              "and", student2.first_name, student2.last_name + "\033[0m\n")
        time.sleep(2)
        self.humanity_level += 1
        student1.energy_level -= 2
        student2.energy_level -= 3
        student1.knowledge_level += 2
        student2.knowledge_level += 2
        print("\x1b[31mMentors humanity has decreased!!!\x1b[0m\n" + self.first_name, self.last_name +
              " has " + str(self.humanity_level) + " humanity points now.")
        time.sleep(0.5)
        print("\x1b[32mStudent " + student1.first_name, student1.last_name + " energy has decreased!\x1b[0m\n" +
              "Actual energy level is", student1.energy_level, "\n")
        time.sleep(0.5)
        print("\x1b[32mStudent " + student2.first_name, student2.last_name + " energy has increased!\x1b[0m\n" +
              "Actual energy level is", student2.energy_level, "\n")
        time.sleep(3)
        os.system('clear')

    def say_joke(self, student):
        print("\033[1mMentor " + self.first_name + " say joke to ", student.first_name, student.last_name)
        choose_joke = random.randint(0, 2)
        if choose_joke == 0:
            print("""
                    FirstJoke(BAD)
            """)
            self.humanity_level += 1
            student.energy_level -= 2
            print("\x1b[32mMentors humanity has decreased!!!\x1b[0m\n" + self.first_name,
                  self.last_name + " has " + str(self.humanity_level) + " humanity points now.")
            time.sleep(0.5)
            print("\x1b[31mStudent " + student.first_name, student.last_name + " energy has decreased!\x1b[0m\n" +
                  "Actual energy level is", student.energy_level, "\n")
            time.sleep(0.5)
            print("\x1b[33mStudent " + student.first_name, student.last_name +
                  "knowledge level is the same... o_O\x1b[0m\n" +
                  "Actual knowledge level is", student.energy_level, "\n")
            time.sleep(3)
        elif choose_joke == 1:
            print("""
                    SecondJoke(Good)
            """)
            self.humanity_level += 2
            student.energy_level += 2
            print("\x1b[31mMentors humanity has increased.\x1b[0m\n" + self.first_name,
                  self.last_name + " has " + str(self.humanity_level) + " humanity points now.")
            time.sleep(0.5)
            print("\x1b[31mStudent " + student.first_name, student.last_name + " energy has decreased!\x1b[0m\n" +
                  "Actual energy level is", student.energy_level, "\n")
            time.sleep(0.5)
            print("\x1b[33mStudent " + student.first_name, student.last_name +
                  "knowledge level is the same... o_O\x1b[0m\n" +
                  "Actual energy level is", student.energy_level, "\n")
            time.sleep(3)
        else:
            print("""
                    ThirdJoke(VeryGood)
            """)
            self.humanity_level += 3
            student.energy_level += 3
            print("\x1b[31mMentors humanity has increased.\x1b[0m\n" + self.first_name,
                  self.last_name + " has " + str(self.humanity_level) + " humanity points now.")
            time.sleep(0.5)
            print("\x1b[31mStudent " + student.first_name, student.last_name + " energy has decreased!\x1b[0m\n" +
                  "Actual energy level is", student.energy_level, "\n")
            time.sleep(0.5)
            print("\x1b[33mStudent " + student.first_name, student.last_name +
                  "knowledge level is the same... o_O\x1b[0m\n" +
                  "Actual energy level is", student.energy_level, "\n")
            time.sleep(3)
        os.system('clear')
