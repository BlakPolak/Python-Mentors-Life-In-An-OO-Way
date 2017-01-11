from person import Person
import csv


class Student(Person):
    """Creates students."""
    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level, knowledge_desire,
                 mood_for_gymnastic):
        Person.__init__(self, first_name, last_name, year_of_birth, gender)
        self.knowledge_level = Person.check_if_correct(knowledge_level, str)
        self.energy_level = Person.check_if_correct(energy_level, str)
        self.knowledge_desire = Person.check_if_correct(knowledge_desire, str)
        self.mood_for_gymnastic = Person.check_if_correct(mood_for_gymnastic, str)

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




