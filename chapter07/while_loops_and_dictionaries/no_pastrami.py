sandwich_order = ["pastrami","cuban","pastrami","turkey on rye","pastrami", "vito"]
finished_sandwiches = []
while sandwich_order:
	sandwich = sandwich_order.pop()
	if sandwich != "pastrami":
		finished_sandwiches.append(sandwich)
		print("I made your " + sandwich)

print(finished_sandwiches)
