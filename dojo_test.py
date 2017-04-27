
from dojo import create_room
from office import Office
from living_space import LivingSpace
from dojo import add_person


def maximum_num_rooms():
    if maximum_num_rooms > 99:
        return Error, "Dojo is at full capacity"
    else:
        return "A room has been created"


class TestCreateRoom(unittest.TestCase):
	def __init__(self):
		self.maximum_num_rooms = maximum_num_rooms

	def create_room(self, room_type, room_name):
		self.AssertIsEqual(room_type, "str")
		room_name.AssertIsEqual(room_name("room_name"), "str")


	def room_type(self,):
		self.room_type == room_type
		if room_type == Office:
			return "Office"
		elif room_type == Living_space:
			return "Living_space"
		else:
		   return "Allocate room_type"
	
	def room_name(self, room_name):
		self.room_name == room_name
		return "room_name"


class TestAddPerson(unittest.TestCase):
	# def add_person(self,person_name, person_type, wants_accomodation):
	# 	self.add_person = add_person
	# 	self.person_name = 
