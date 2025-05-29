current_users = ["matt","lucy","brendon","david","aaron"]
new_users = ["harm","David","jonny","nick","mathew"]

if new_users:
	if current_users:
		for user in new_users:
			if user.lower() not in current_users:
				print("username available!")
			else:
				print("username already used; pick another")
