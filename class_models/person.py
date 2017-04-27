class Person(subject):
    """A Person exists under Dojo"""

    list_of_people = []

    def __init__(self, person_type):
        self.person_type = person_type

    def person_type(self):

        if person_type == Staff:
            return staff_name, "staff"

        elif person_type == Fellow:
            return fello_name, "fellow"

        else:
            return "Error passing person"
