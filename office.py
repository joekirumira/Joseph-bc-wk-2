from room import Room


class Office(Room):
    """An office under Rooms"""

    def __init__(self, room_name, room_type):
        # self.Office = len(__init__ self.Office)
        super().__init__(room_name, room_type)
        self.office_capacity = 6
        self.office_name = {}

    def add_office(self, office_name):
        # self.add_office == len(__init__ self.Office) +1
        self.office_name = office_name

        if 5 < self.office_capacity:
            return "office has reached full capacity"
        else:
            return office_name, "new office has been created"
