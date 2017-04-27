from person import Person


class Staff(Person):
    """A Staff exists under Person"""

    list_of_staff = []

    def __init__(self, staff_name, accomodation):
        self.staff_name = staff_name
        self.accomodation = False

