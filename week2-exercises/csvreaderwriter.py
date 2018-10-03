file = open("footballers.csv")
players = open("players1.txt","w")

for line in file:
	row = line.strip().split(",")
	write = print(row[0] + " is a player of " + row[1] + " worth " + row[2] + " million dollars.") #basic assignment
	convert = ''.join(row[2]) #converting into string so I can edit it with .replace (instead of just changing the string earlier) 
	replace = "$" + convert + ".000.000" # You can also convert to int and *10000 which I do later, benefit of current is the readability with the dots and .replace() practice. 
	newrow = row[0] + " is a player of " + row[1] + " worth " + replace + "\n"
	players.write(newrow)

# changing from (over)writing to appending
players = open("players1.txt", "a")
file = open("footballers.csv", "a")

# new input
newplayername = input("\nWhat footballer (name) do you want to add to the file? ").strip()
newplayerclub = input("What club does this player currently play for? ").strip()
newplayervalue = int(input("What is the players value in milli0ns without the zer0s: ").strip()) 

#writing to both files, different ways of displaying the values
newinputtxt = newplayername + " is a player of " + newplayerclub + " worth $" + str(newplayervalue * 1000000) + "\n" # harder to read in file, no decimal thousand seperator 
newinputcsv = newplayername + "," + newplayerclub + "," + str(newplayervalue) + "\n"  

players.write(newinputtxt)
file.write(newinputcsv)

players.close()
file.close()

print("Everything should be there in the files!")
