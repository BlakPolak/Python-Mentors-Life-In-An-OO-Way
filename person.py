

class Person:
    def __init__(self, first_name, last_name, year_of_birth, gender):
        self.check_if_correct(first_name, str)
        self.first_name = first_name
        self.check_if_correct(last_name, str)
        self.last_name = last_name
        self.check_if_correct(year_of_birth, int)
        self.year_of_birth = year_of_birth
        self.check_gender(gender)
        self.gender = gender

    @staticmethod
    def check_if_correct( validate, check_type):
        if type(validate) != check_type:
            raise TypeError


    def check_gender(self, gender):
        gender_list = ['male', 'female', 'notsure']
        if gender not in gender_list:
            raise TypeError

