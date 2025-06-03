topping = ""
print("Tell me the pizza topping you want! ('quit' to exit)")
while topping != 'quit':
	topping = input()
	if topping != 'quit':
		print("I've added " + topping + " to your pizza!")
