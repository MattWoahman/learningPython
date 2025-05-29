usernames = ['admin', 'matt', 'lucy', 'system', 'brendon']
usernames = []
if usernames:	
	for username in usernames:
		if username == 'admin':
			print("Hello Admin! Would you like to see a status report?")
		else:
			print("Hello " + username + ", good to see you!")
else:
	print("We need to find some users!")
