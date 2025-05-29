numbers = list(range(1, 1000001))

print("The first three numbers in the list are:")
for number in numbers[:3]:
	print(number)

print("\n The items from the middle of the list are:")
middle_start = round((len(numbers)/2)-2)
middle_end = round((len(numbers)/2)+1)

for number in numbers[middle_start:middle_end]:
	print(number)

print("\n The last three items in the list are:")
for number in numbers[-3:]:
	print(number)
