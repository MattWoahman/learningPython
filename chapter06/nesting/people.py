person_1 = {
	'first_name':'Lucy',
	'last_name':'Ray',
	'age':'22',
	'city':'Portland',
	}
person_2 = {
	'first_name':'Matt',
	'last_name':'Homan',
	'age':'23',
	'city':'Royse City',
	}
person_3 = {
	'first_name':'Brendon',
	'last_name':'Kofink',
	'age':'22',
	'city':'Flower Mound',
	}

people = [ person_1, person_2, person_3 ]

for person in people:
	print("First Name: " + person['first_name'])
	print("Last Name: " + person['last_name'])
	print("Age: " + person['age'])
	print("City: " + person['city'])
	print("\n")
