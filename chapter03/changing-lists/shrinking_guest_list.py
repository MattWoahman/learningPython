guestList = ['Jeff Donahoo', 'Pat Hynan', 'Shaun Hutton']
print(guestList[0] + ", you're invited to dinner!")
print(guestList[1] + ", you're invited to dinner!")
print(guestList[2] + ", you're invited to dinner!")

print("\n" + guestList[0] + " can't make it!")
guestList[0] = "Jeff Blake"

print("\n" + guestList[0] + ", you're invited to dinner!")
print(guestList[1] + ", you're invited to dinner!")
print(guestList[2] + ", you're invited to dinner!")

print("\n We found a bigger dinner table! \n")
guestList.insert(0, "Pablo Rivas")
guestList.insert(2, "Sheila Cernosek")
guestList.insert(-1, "Cody Holt")

print(guestList[0] + ", you're invited to dinner!")
print(guestList[1] + ", you're invited to dinner!")
print(guestList[2] + ", you're invited to dinner!")
print(guestList[3] + ", you're invited to dinner!")
print(guestList[4] + ", you're invited to dinner!")
print(guestList[5] + ", you're invited to dinner!")

print("\n We have to shrink the list to two!\n")

popped_guest = guestList.pop()
print("Sorry, " + popped_guest + ", we ran out of room!")
popped_guest = guestList.pop()
print("Sorry, " + popped_guest + ", we ran out of room!")
popped_guest = guestList.pop()
print("Sorry, " + popped_guest + ", we ran out of room!\n")
popped_guest = guestList.pop()
print("Sorry, " + popped_guest + ", we ran out of room!\n")


print("Don't worry, " + guestList[0] + " & " + guestList[1] + ", you're still invited!")
del guestList[1]
del guestList[0]
print(guestList)  
