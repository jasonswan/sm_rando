# Author - Aremath
# test function to ensure parser is working properly.

import parse_rooms

if __name__ == "__main__":

	rooms = parse_rooms.parse_rooms("encoding/rooms.txt")
	#rooms = parser.parse_rooms("encoding/test.txt")

	#print rooms["West_Ocean"][0].graph
	print rooms["Frog_Speedway"][0].graph

	# TODO: actually test something too :P do stuff
