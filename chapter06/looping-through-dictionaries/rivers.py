rivers = {
	"nile":"egypt",
	"misissippi":"usa",
	"thames":"england",
	}
for key, value in rivers.items():
	print("The " + key + " runs through " + value)

print("\n Rivers:")
for key in rivers:
	print("\t" + key)

print("\n Countries:")
for value in rivers.values():
	print("\t" + value)
