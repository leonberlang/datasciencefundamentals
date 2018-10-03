wrong_words = ["kapod", "viets", "outo", "telefisie", "brommur", "stopbort", "voedbal"]
right_words = ["kapot", "fiets", "auto", "televisie", "brommer", "stopbord", "voetbal"]

sentence = input("Enter your sentence here: ").lower().strip().split()
newsentence = []

#
#spellchecking by going through all the words and getting the replacement one
for word in sentence:
	#index = index + 1
	if word in wrong_words:
		print("Hey that's not right!")
		location = wrong_words.index(word)
		replacement = right_words[location]
		print("You should use " + right_words[location] + " instead of " + wrong_words[location])
		newsentence.append(replacement)
	else:
		newsentence.append(word)

#dit kan niet: newsentence.replace(wrong_words[index], right_words[index]) - want kan niet editen in list

newsentence = " ".join(newsentence)
print("\nYour sentence should be like this:" + "\n" + newsentence)
