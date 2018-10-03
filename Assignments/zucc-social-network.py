#Welcome the user and getting getting clean usable data
print("Hey! Welcome to my social network. What's your FIRST name?")
firstname = input("My FIRST name is: ").lower().capitalize().strip()
print("\nWelcome " + firstname + "! Nice to see you. What is your (last) name?")
name = input("My name is: ").lower().capitalize().strip()
fullname = firstname + (" ") + name

if name == "Berlang":
	print("\nWelcome fellow Berlang family member!")

birthyear = input("In what year were you born? ").strip()

# Making sure the input is correct, so users aren't just putting a high or low number into it and breaking the system.
# I.e.: if the user would put 2 he would be old enough because the way it's calculated.
while float(birthyear) < 1900 or float(birthyear) > 2018:
	birthyear = input("Stop lying! In what year were you actually born? ")	

#Calculating age based on birthyear to filter out underage users
agereq = 18
birthcalc = 2018 - int(birthyear)

#Gatekeeping but welcoming them in X years when they are old enough
agediff = str(agereq - birthcalc) 
if birthcalc >= agereq:
	print("\nYou are allowed to proceed!")
else:
	print("\nYou are too young to proceed, I'm sorry! See you in " + agediff + " years!") 
	quit()

# Restricting genders because processability
genderlist = ["Male", "Female", "Other"]
gender = input("\nWhat gender do you consider yourself to be a part of?\nPlease choose between Male, Female and Other.\n").lower().capitalize().strip()
while gender not in genderlist:
	gender = input("\nWhat gender do you consider yourself to be a part of?\nPlease choose between Male, Female and Other.\n").lower().capitalize().strip()
else:
	print("\nVery good! We're almost done setting up your account.\nPlease enter your email down below to confirm your signup.")

# Asking for real email addresses to stop spam account creation (more valuable accounts)
email = input("Email Address: ")
while ("@") and (".") not in email:
	print("Please enter a real email address.")
	email = input("Email Address: ")
else:
	print("\nPlease check your email later to confirm your singup! For now you can proceed with the final (optional) step.") 

# Asking for 2 factor authentication (more valuable accounts)
print("\nWe recommend you set up 2factor authentication for the security of your account. If you would like to skip this part, please write 'skip'.\n")
twofactorauth = input("Mobile phone number: ").lower().strip()
if twofactorauth == ("skip"):
	twofactorauth.replace("skip", " No phone number set up for 2 factor authentication.")
	phonesetup = 0
else:
	print("\nThank you for setting up 2 factor authentication.")
	phonesetup = 2

print("\nSignup is now done.")

# Calculating the social value / advertisement worth of a certain user based on age, gender, name length, 2 fact auth, email
# the higher the number the better the value
agevalue = birthcalc / 118 # 118 is hoogste mogelijk leeftijd
gendervalue = 2 # no difference between genders
namevalue = len(fullname) / 15 # avg naam   
if ".nl" in email: 
	emailvalue = 2 #bonus voor nationanlism
else:
	emailvalue = 1

#total value	
socialvalue = agevalue + gendervalue + namevalue + phonesetup + emailvalue

print("\nBecause we care about your privacy - or maybe because of the European GDPR law \nwe have to tell you can ask us for a copy of your data and/or remove it from our database.")

#making it a function so its easy to repeat until no more questions
def gdprfunction():
	#making the variables global so they work outside the function
	global firstname
	global fullname
	global birthcalc
	global birthyear
	global gender
	global socialvalue
	global email
	global twofactorauth

	#asking for input
	gdpr = input("If you would like to like to get a copy of your data, type 'SHOWDATA'. If you would like to remove your data, type 'REMOVE'. You can quit by typing literally anything else.\n").upper()
	
	if gdpr == "SHOWDATA":
		print("We have the following information about you: ")
		print("Full name: " + fullname)
		print("Age: " + str(birthcalc) + " (born in " + birthyear + ")")
		print("Gender: " + gender)
		print("Your social value: " + str(socialvalue))
		print("Email: " + email)
		print("Phone NR: " + twofactorauth)
		gdprfunction()

	elif gdpr == "REMOVE":
		firstname = ""
		name = ""
		fullname = ""
		gender = ""
		birthyear = ""
		birthcalc = ""
		email = ""
		twofactorauth = ""
		socialvalue = ""
		print("All data has been removed.")
		gdprfunction()

	else: # if the user isn't interested in either showing oro removing their data.
		print("Goodbye! See you next time.")
		quit()

gdprfunction()
