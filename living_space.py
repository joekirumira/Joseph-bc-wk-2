from room import Room


class LivingSpace(Room):
    """A Living space under Rooms"""

    def __init__(self):
        # self.living_space == len(__init__ self.living_space)
        self.living_space = len(self.living_space) + 1
        self.living_space_capacity = 4
        self.living_space_name = {}

    def add_living_space(self, living_space_name):
        self.living_space_name = living_space_name

        if self.living_space_capacity > 3:
            return "Living space has reached full capacity"
        else:
            return living_space_name, "Living space has been created"
