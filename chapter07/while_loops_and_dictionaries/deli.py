sandwich_order = ["cuban","turkey on rye", "vito"]
finished_sandwiches = []
while sandwich_order:
	sandwich = sandwich_order.pop()
	finished_sandwiches.append(sandwich)
	print("I made your " + sandwich)

print(finished_sandwiches)
