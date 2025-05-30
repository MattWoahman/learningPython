favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
people = {'jen','brendon','lucy','edward','matt','phil'}

for person in people:
	if person in favorite_languages.keys():
		print("Thank you, " + person +", for taking our poll!")
	else:
		print(person + ", please take our poll!")

