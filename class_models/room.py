from office import Office
from living_space import LivingSpace
# from dojo_test import TestCreateRoom

class Room(object):
	"""Rooms in Dojo"""

	def __init__(self, room_name, room_type):
		self.room_name = room_name
		self.room_type = room_type
	
	def room_name(self):
		return room_name

	def room_type(self):
	    return room_type	