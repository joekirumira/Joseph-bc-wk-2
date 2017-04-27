from room import Room


class LivingSpace(Room):
    """A Living space under Rooms"""

        list_of _living_space = []

    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_capacity = 4

    def add_living_space(self, living_space_name, living_space_capacity):
        self.living_space_name = living_space_name
        self.living_space_capacity = living_space_capacity

        if self.living_space_capacity > 3:
            return "Living space has reached full capacity"
        else:
            return living_space_name, "Living space has been created"
