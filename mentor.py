from person import Person
import csv


class Mentor(Person):
    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, energy_level, humanity_level):
        Person.__init__(self, first_name, last_name, year_of_birth, gender)
        self.nickname = nickname
        self.energy_level = energy_level
        self.humanity_level = humanity_level

    @staticmethod
    def create_by_csv(filename="data/mentors.csv"):
        """Loading data from csv file"""
        list_of_mentors_object = []
        with open(filename) as file:
            file_reader =  csv.reader(file)
            for data in file_reader:
                list_of_mentors_object.append(Mentor(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        return list_of_mentors_object


# Mentor.create_by_csv(filename="data/mentors.csv")


