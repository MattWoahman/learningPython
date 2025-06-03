while True:
	print("What's your age?")
	age = input()
	if int(age) < 3:
		print("Your ticket is free!")
	elif int(age) < 21:
		print("Your ticket is $10!")
	else:
		print("Your ticket is $15!")
