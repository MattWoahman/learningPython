poll = 'true'
places = []
while poll == "true":
	print("If you could visit one place in the world, where would you go?")
	place = input()
	places.append(place)
	print("\n Do you have another place? [y/n]")
	ans = input()
	if ans == 'n':
		poll = 'false'

for place in places:
	print(place)
