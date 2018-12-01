# Import the all modules needed
import csv
import os
import random

# Check if there is a file called 'people.csv'
if os.path.isfile("people.csv"):
    print("There is a file with that name. We can proceed.\n")
else:
    print("No such file was found. Please make sure people.csv is in the same folder as this program.\n")
    exit()

# Read the data from this file and convert it to a multidimensional list
list_count = []
add_name = ['Ivanka', 'Erik', 'Tiffany', 'Donald', 'Barron']

# Initial conversion to list
file = open("people.csv", "r")
for line in file:
    row = line.strip().split(",")
    list_count.append(row)
file.close()

# Printing the entries
def print_entries():
    people_index = 0
    print("Current entries:")
    for line in list_count:
        print(f'{people_index}: {line[0]} {line[1]}')
        people_index = people_index + 1 #counting the people in the list

    print(f"\nThere are {str(people_index)} people in this list.")

def save_to_file():
    file = open("people.csv", "w")
    for information in list_count:
        info_join = str(",".join(information) + "\n")      
        file.write(info_join)  
    file.close()
    print_entries()
    
# Showing the current entries.
print_entries()

# Ask which option they would like to choose
def print_allowed_entries():
    print("What would you like to do?\n")
    print("To remove a person: enter '1'")
    print("To add a person: enter '2'")
    print("To quit the program: enter '3'\n")

# Keeping the user in the program with a while loop.
user_input = True
while user_input == True:
    
    # Create a loop with input validation 
    print_allowed_entries()
    answer = input("Enter your selection here: ").strip()
    allowed_entries = ["1","2","3"]
    while answer not in allowed_entries:
        print("That input is incorrect.  Please enter one of the following:")
        print_allowed_entries()
        answer = input("Enter your selection here: ").strip()

    # Remove a person from the list by using the indexnumber
    if answer == "1" :
        total_entries = len(list_count)
        remove_person = int(input("Who do you want to remove? Type the indexnumber: ").strip())
        while remove_person >= total_entries or remove_person <0: # preventing wrong entry
            print("Please choose a viable option out of the list. That entry is incorrect.")
            remove_person = int(input("Who do you want to remove? Type the indexnumber: ").strip())
        removed_name = list_count[remove_person][0]
        removed_number = list_count[remove_person][1]
        list_count.pop(remove_person)
        print(f"\nYou have removed {removed_name} (index nr {remove_person}) with (phone)number {removed_number}\n")
        save_to_file()

    # Add a person to the list by creating a random name and a random number
    if answer == "2":
        addname = random.choice(add_name).split()
        addnumber = str(random.randint(10000,1000000)).split()
        list_count.append(addname + addnumber)
        print(f' {addname[0]} with the number {addnumber[0]} has been added to the list.')
        save_to_file()

    # If the user chooses ‘Quit the program’ the program should quit
    if answer == "3":
        user_input = False
        print("Goodbye")
        exit()