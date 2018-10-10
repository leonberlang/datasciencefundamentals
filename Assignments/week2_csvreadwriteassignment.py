politicians = open("politicians.csv") # with open("politicians.csv") as f 
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
		people = people + 1

print("\nThere are " + str(people) + " total people in the database.")

def mutations(): # function so you can start over again with everything until 'quit'
	global oglist
	questionoptions = ["remove","add","save","quit"]
	questioninput = input("\nYou can do 3 things: REMOVE, ADD or QUIT the program. What do you want to do?").strip().lower()

	while questioninput not in questionoptions:
		questioninput = input("\nPlease choose between the following 4 options: REMOVE or ADD to the database or QUIT the program. What do you want to do?").strip().lower()

	if questioninput == "remove":
		rpeople = 0
		rpoliticians = open("politicians.csv")
		print("These are the current entries:")
		
		for rline in rpoliticians:
				rrow = rline.strip().split(",")
				rfirstname = rrow[0]
				rname = rrow[1]
				rbirthyear = rrow[2]
				rpoliticalparty = rrow[3]
				print("[" + str(rpeople) + "] " + rfirstname + " " + rname + " was born in " + rbirthyear + " and member of the " + rpoliticalparty + " party.")
				rpeople = (rpeople + 1)
		
		removedrow = int(input("\nWhat row dou you want to have removed? Row "))
		oglist.pop(removedrow)		
		rpoliticians = open("politicians.csv","w")
		
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
