sentence = input("your sentence here: ")
sentencelength = len(sentence)
calc25 = round(sentencelength * .25)
calc75 = round(sentencelength * .75) 

slicedsentence = sentence[calc25:calc75] 
print("Middle part of the string sentence is: " + slicedsentence)

#convert
listsentence = sentence.split()

#list doin the same stuff
listsentencelength = len(listsentence)
calc25list = round(listsentencelength * .25)
calc75list = round(listsentencelength * .75)
slicedlistsentence = " ".join(listsentence[calc25list:calc75list])

print("Middle part of the new sliced sentence is: " + slicedlistsentence) 
