from student import Student
from mentor import Mentor
import time

class CodecoolClass:
    """
    This class represents a real class @ Codecool, containing mentors and students working at the class.

    Args:
        location: stores the city where the the class started
        year: stores the year when the class started
        mentors: stores the mentors of the class
        students: stores the students of the class

    """

    def __init__(self, location, year, students, mentors):
        """
        Initialize object args

            Args:
                location: stores the city where the the class started
                year: stores the year when the class started
                mentors: stores the mentors of the class
                students: stores the students of the class

            Returns:
            None
        """
        self.location = location
        self.year = year
        self.students = students
        self.mentors = mentors


    @staticmethod
    def create_local_school():
        """
        Creates a CodecoolClass object having some real-life data from the implementer students' real class.

        Args:
            None

        Returns:
            CodecoolClass object
        """
        students = Student.create_by_csv("data/students.csv")
        mentors = Mentor.create_by_csv("data/mentors.csv")
        return students, mentors

    def find_student_by_full_name(self, full_name):
        """
        Searches for a student named 'full name' from student database

        Args:
            full_name: holds the full name of the student to be found

        Returns:
            Student object
        """
        name_list = full_name.split(" ")
        for student in self.students:
            if student.first_name == name_list[0]:
                if student.last_name == name_list[1]:
                    print(student.first_name, student.last_name + " found in our class.")
                    return student
        print(full_name + " student is not in our class.")
        return False

    def find_mentor_by_full_name(self, full_name):
        """
        Searches for a mentor named 'full name' from mentor database

        Args:
            full_name: holds the full name of the mentor to be found

        Returns:
            Mentor object
            """
        name_list = full_name.split(" ")
        for mentor in self.mentors:
            if mentor.first_name == name_list[0]:
                if mentor.last_name == name_list[1]:
                    print(mentor.first_name, mentor.last_name + " mentor found in our class.")
                    return mentor
        print(full_name + " mentor is not in our class.")
        return False


    def check_overall_energy(self):
        """
        Displays energy for all school members

        Args:
            None

        Returns:
            None
        """
        energy = 0
        for student in self.students:
            energy += int(student.energy_level)
        for mentor in self.mentors:
            energy += int(mentor.energy_level)
        print("Overall energy equals ", energy)


    def is_any_mentor_became_human(self):
        """
        Checks if mentor became human being (when his humanity_level variable reaches 10).

        Args:
            None

        Returns:
            True if mentor reaches humanity_level :10, False if not
        """
        for mentor in self.mentors:
            if mentor.humanity_level >= 10:
                print("\033[44m"+mentor.first_name, mentor.last_name+" called "+ mentor.nickname+" has become human "
                    "Is ready to deliver to new Codecool facility!", mentor.first_name, mentor.last_name,
                    "may the Force be with You!\033[0m")
                time.sleep(3)
                return True
        return False
