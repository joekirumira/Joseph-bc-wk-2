from office import Office
from living_space import LivingSpace
from room import Room
from fellow import Fellow
from staff import  Staff
from person import Person


class Dojo(object)
	""" Class Dojo """
	def __init__(self):
		maximum_num_rooms = 100
		self.list_of_rooms = []
		self.list_of_people = []

	def create_room(self, room_type, room_name):
		self.create_room = create_room
		self.room_type = room_type
		self.room_name = room_name

		if room_type == "office":
			office = Office(office_name)
			self.list_of_rooms.Append(office)
			return "You have created room '+room_name+' which  an office"
		elif room_type == "living_space":
			living_space = LivingSpace(living_space_name)
			self.list_of_rooms.Append(living_space)
            return ("You have created room '+room_name+' which is a living space")

    def room_exists(self, room_name):
        for room in self.list_of_rooms:
            if room.room_name ==room_name:
                return True
            else:
                return False

    def maximum_capacity_of_Dojo(self,num_of_rooms):
        self.num_of_rooms = num_of_rooms
        if num_of_rooms = 100:
            return True

    def add_person(self, first_name, sur_name, person_type, need_livingspace):
        

