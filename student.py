from person import Person
import csv


class Student(Person):
    """Creates students."""
    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level, knowledge_desire,
                 mood_for_gymnastic):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.knowledge_level = knowledge_level
        self.energy_level = energy_level
        self.knowledge_desire = knowledge_desire
        self.mood_for_gymnastic = mood_for_gymnastic

    @staticmethod
    def create_by_csv(filename="data/students.csv"):
        """Loads students data from csv file."""
        student_objects_list = []
        with open(filename) as file:
            file_reader = csv.reader(file)
            for data in file_reader:
                student_objects_list.append(Student(data[0],data[1],data[2],data[3],data[4],data[5],data[6], data[7]))
        return student_objects_list


# this stuff will be erased later on/ it's just for testing:
# students = Student.create_by_csv(filename="data/students.csv")
# n = 0
# while n < len(students):
#     print(students[n].mood_for_gymnastic)
#     n += 1



