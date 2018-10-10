politicians = open("politicians.csv") # or open("politicians.csv") as f 
people = 0 
oglist = []

#printing the available options and appending them into a multi-dimensional list so it's usable
for line in politicians:
		row = line.strip().split(",")
		oglist.append(row)
		firstname = row[0]
		name = row[1]
		birthyear = row[2]
		politicalparty = row[3]
		print("[" + str(people) + "] " + firstname + " " + name + " was born in " + birthyear + " and member of the " + politicalparty + " party.")
		people = people + 1 #counting people

print("\nThere are " + str(people) + " total people in the database.")

def mutations(): # function so you can start over again with everything until 'quit'
	global oglist
	questionoptions = ["remove","add","save","quit"]
	questioninput = input("\nYou can do 3 things: REMOVE, ADD or QUIT the program. What do you want to do?").strip().lower()

	while questioninput not in questionoptions:
		questioninput = input("\nPlease choose between the following 4 options: REMOVE or ADD to the database or QUIT the program. What do you want to do?").strip().lower()

	if questioninput == "remove":
		r_people = 0
		r_politicians = open("politicians.csv")
		print("These are the current entries:")
		
		for r_line in rpoliticians: #giving the current options in file, because might be already added (add doesnt write in memory) - might need to change that so I can just write out of the list and just replace there aswell
				r_row = r_line.strip().split(",")
				r_firstname = r_row[0]
				r_name = r_row[1]
				r_birthyear = r_row[2]
				r_politicalparty = r_row[3]
				print("[" + str(r_people) + "] " + r_firstname + " " + r_name + " was born in " + r_birthyear + " and member of the " + r_politicalparty + " party.")
				r_people = (r_people + 1)
		
		removedrow = int(input("\nWhat row dou you want to have removed? Row "))
		oglist.pop(removedrow)		
		r_politicians = open("politicians.csv","w") #changing it to writing instead of reading
		
		for line in oglist:
			converted = ",".join(line)
			converted = converted + "\n"
			rpoliticians.write(converted)	
		rpoliticians.close()
		print("\nRemoved out of the database.")
		mutations()

	if questioninput == "add":
		addfirstname = input("What is the first name?").lower().capitalize().strip()
		addname = input("What is the name?").lower().capitalize().strip()
		addbirthyear = input("What is the birth year?")
		addpoliticalparty = input("What political party is this person part of?").lower().capitalize().strip()
		politicians = open("politicians.csv","a")
		newpolitician = addfirstname + "," + addname + "," + addbirthyear + "," + addpoliticalparty + "\n"
		newpolitician2 = newpolitician.split()
		newentry = oglist.append(newpolitician2)
		print(oglist)
		politicians.write(newpolitician)
		politicians.close()
		print("The user has been added to the database.")
		mutations()
				
	if questioninput == "quit":
		print("\nGoodbye, see you next time!")
		quit()

mutations()
