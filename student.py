import csv
from person import Person


class Student(Person):
    """
    This class represents class real student in Codecool

        Args:
            knowledge_level: stores student programming level
            energy_level: stores student energy
            knowledge_desire: describes students hunger for knowledge
            mood_for_gymnastic: stores students attitude for gymnastics

    """
    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level, knowledge_desire,
                 mood_for_gymnastic):
        Person.__init__(self, first_name, last_name, year_of_birth, gender)
        self.knowledge_level = Person.check_if_correct(knowledge_level, str)
        self.energy_level = Person.check_if_correct(energy_level, str)
        self.knowledge_desire = Person.check_if_correct(knowledge_desire, str)
        self.mood_for_gymnastic = Person.check_if_correct(mood_for_gymnastic, str)

    def __str__(self):
        return self.first_name+" "+self.last_name


    @staticmethod
    def create_by_csv(filename="data/students.csv"):
        """
        Loads students data from csv file.

        Args:
            filename: file path for csv file

        Returns:
            List of Student objects
        """
        student_objects_list = []
        with open(filename) as file:
            file_reader = csv.reader(file)
            for data in file_reader:
                student_objects_list.append(Student(data[0],data[1],data[2],data[3],data[4],data[5],data[6], data[7]))
        return student_objects_list





