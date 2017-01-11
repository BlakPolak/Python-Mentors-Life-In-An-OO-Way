from person import Person


class Mentor(Person):
    def __init__(self, nickname, energy_level, humanity_level,
                 first_name, last_name, year_of_birth, gender):
        self.nickname = nickname
        self.energy_level = energy_level
        self.humanity_level = humanity_level
        Person.__init__(self, first_name, last_name, year_of_birth, gender)

    @staticmethod
    def create_by_csv(csv_filename):
        mentors = []
        handler = open(csv_filename, "r")
        data = handler.readlines()
        for line in data:
            data_list = line.split(",")
            new_mentor = Mentor(data_list[4], data_list[5], data_list[6], data_list[0], data_list[1],
                                data_list[2], data_list[3])
            mentors.append(new_mentor)
        return mentors
