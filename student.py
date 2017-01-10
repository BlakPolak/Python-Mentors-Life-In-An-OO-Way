from person import Person


class Student(Person):
    def __init__(self, knowledge_level, energy_level, knowledge_desire, mood_for_gymnastic,
                 first_name, last_name, year_of_birth, gender):
        self.knowledge_level = knowledge_level
        self.energy_level = energy_level
        self.knowledge_desire = knowledge_desire
        self.mood_for_gymnastic = mood_for_gymnastic
        Person.__init__(self, first_name, last_name, year_of_birth, gender)

    @staticmethod
    def create_by_csv(csv_filename):
        students = []
        handler = open(csv_filename, "r")
        data = handler.readlines()
        for line in data:
            data_list = line.split(",")
            new_student = Student(data_list[4], data_list[5], data_list[6], data_list[7], data_list[0],
                                  data_list[1], data_list[2], data_list[3])
            students.append(new_student)
        return students
