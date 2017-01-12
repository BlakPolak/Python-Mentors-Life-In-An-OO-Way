
class Person:
    """
    Base class for each person in Codecool

        Args:
            first_name: stores the first name of person
            last_name: stores the last name of person
            year_of_birth: stores person's year of birth.
            gender: stores the person gender
    """
    def __init__(self, first_name, last_name, year_of_birth, gender):
        self.check_if_correct(first_name, str)
        self.first_name = first_name
        self.check_if_correct(last_name, str)
        self.last_name = last_name
        self.year_of_birth = self.check_if_correct(year_of_birth, str)
        self.check_gender(gender)
        self.gender = gender

    @staticmethod
    def check_if_correct(validate, check_type):
        """
        Checks if variable is expected type and convert it to integer type if it contains just digits

        Args:
            validate: variable to check
            check_type: expected type of variable

        Returns:
            validated variable
        """
        if type(validate) != check_type:
            raise TypeError
        elif type(validate) == check_type:
            if validate.isdigit():
                validate = int(validate)
                return validate
            elif all(i.isalpha() or i.isspace() for i in validate):
                return validate
            else:
                raise TypeError



    def check_gender(self, gender):
        """
        Checks if variable is correct type of gender, if not - it raises an error

        Args:
            gender: variable to check

        Returns:
            None
        """
        gender_list = ['male', 'female', 'not sure']
        if gender.lower() not in gender_list:
            raise TypeError

