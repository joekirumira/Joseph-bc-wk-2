from room import Room


class Office(Room):
    """An office under Rooms"""

    list_of_rooms = []

    def __init__(self, room_name, room_type):
        super().__init__(room_name, room_type)
        self.office_capacity = 6
        self.office_name = ofiice_name

    def add_office(self, office_name):
        self.office_name = office_name

        if 5 < self.office_capacity:
            return "office has reached full capacity"
        else:
            return office_name, "new office has been created"
