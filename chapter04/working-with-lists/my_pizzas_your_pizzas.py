
pizzas = ['cheese', 'pepperoni', 'sausage']
for pizza in pizzas:
    print("I like " + pizza + " pizza!")
print ("I really like pizza!")

friends_pizzas = pizzas[:]

pizzas.append("bbq ranch")
friends_pizzas.append("veggie")

print("My favorite pizzas are")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
	print(pizza)

