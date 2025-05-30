lucy = {
	"name":"lucy",
	"fav_1":"24",
	"fav_2":"35",
	}
matt = {
	"name":"matt",
	"fav_1":"42",
	"fav_2":"54",
	}
brendon = {
	"name":"brendon",
	"fav_1":"45",
	"fav_2":"54",
	}
aaron = {
	"name":"aaron",
	"fav_1":"3",
	"fav_2":"2",
	}
david = {
	"name":"david",
	"fav_1":"252",
	"fav_2":"525",
	}

people = [ matt, lucy, brendon, aaron, david ]

for person in people:
	print(person['name'] + ":")
	print("\t favorite number one: " + person['fav_1'])
	print("\t favorite number two: " + person['fav_2'])
