class Office():
    """An office under Rooms"""

    def __init__(self):
        # self.Office = len(__init__ self.Office)
        self.office_capacity = 6
        self.office_name = {}

    def add_office(self, office_name):
        # self.add_office == len(__init__ self.Office) +1
        self.office_name = office_name	


        if self.office_capacity > 5:
            return "office has reached full capacity"
        else:
            return (office_name, "new office has been created")
