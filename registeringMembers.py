from datetime import date

def introduction():
	print("-------------------------------------")
	print("WELCOME TO THE SYSTEM, ADMINISTRATOR!")
	print("-------------------------------------")
	print("Created by: LumiconBert")
	print("Date: ", date.today())

namesList = []

def membersList():
	if len(namesList) != 1:
		print(f"You have {len(namesList)} members.")
		print("Members: ")
	else:
		print(f"You have {len(namesList)} member.")
		print("Member: ")

	count = 0
	while count < len(namesList):
		print(f"{count + 1}. {namesList[count]}")
		count += 1

introduction()
membersList()

while True:
	options = ("Add new member(s)", "Delete existing member(s)", "List existing member(s)", "Exit")
	print("Menu: ")
	for index, item in enumerate(options):
		print(f"{str(index+1)}. {item}")
	choice = int(input("Choice: ")) - 1
	if choice == 0:
		while True:
			try:
				newMemberNumbers = int(input("Number(s) of new members: "))
				if type(newMemberNumbers) == int:
					break
			except ValueError:
				print("Please input numbers!")
		for i in range(newMemberNumbers):
			while True:
				newMember = input(f"Full Name of member {i+1}: ")
				if newMember != '':
					break
				else:
					print("Please do not empty the field")
			namesList.append(newMember)
	elif choice == 1:
		print("This option is not available yet.")
	elif choice == 2:
		print()
		membersList()
	elif choice == 3:
		break
	else:
		print("Error")
	print("-------------------------------------")
	print()
