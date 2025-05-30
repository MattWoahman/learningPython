lizzie = {
	"owner":"Matt",
	"kind":"Dog",
	}
sugar = {
	"owner":"Ellie",
	"kind":"Dog",
	}
dead_fish = {
	"owner":"Aaron",
	"kind":"Glo-fish",
	}
pebble = {
	"owner":"Macy",
	"kind":"cat",
	}
pets = [lizzie,  sugar, dead_fish, pebble]

for pet in pets: 
	print("Animal Owner: " + pet['owner'])
	print("Animal Kind: " + pet['kind'])
