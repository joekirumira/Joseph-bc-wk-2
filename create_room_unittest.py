import unittest

from Dojo import create_room

class TestCreateRoom(unittest.TestCase):
	def create_room(room_type, room_name):
		room_type.AssertIsEqual(room_type("room_type"), "str")

