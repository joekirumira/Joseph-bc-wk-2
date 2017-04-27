from class_models.fellow import Fellow
from person import Person


class Fellow(Person):
    """A Fellow exists under Person"""

    def __init__(self, fellow_name, accomodation):
        self.fellow_accomodation = accomodation
        self.fellow_name = fellow_name

    fellow = Fellow("bad", False)
