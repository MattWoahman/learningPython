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
