import unittest
from office import Office
from dojo import Dojo


	def maximum_capacity_of_Dojo (self):
    	if num_of_rooms > 99:
    	self.assert



class TestCreateRoom(unittest.TestCase):

	def create_room(self, room_type, room_name):
		self.AssertIsEqual(room_type, "str")
		self.AssertIsEqual(room_name, "str")

	def test_create_room_complete(self):
		dojo = Dojo()
		init_room_count = len(dojo.list_of_rooms)
		black_office = dojo.create_room("Black", "office")
		self.assertTrue(black_office, "An office called black has been created")
		new_room_count = len(dojo.list_of_rooms)
		self.assertEqual(new_room_count - init_room_count, >1)

	def test_room_already_exists(self):
		dojo = Dojo()
		black_office = dojo.create_room("Black", "office")
		black_exists = dojo.room_exists("Black")




class TestAddPerson(unittest.TestCase):
	# def add_person(self,person_name, person_type, wants_accomodation):
