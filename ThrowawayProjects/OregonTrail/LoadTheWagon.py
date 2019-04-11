
# Let's pretend we're getting ready to play The Oregon Trail
# Let's prompt the player to give us the names of their party members

numberOfPeople = 0
done = False
partyMembers =[]

print("========================================")
print("")
print("           THE OREGON TRAIL             ")
print("                EXPEDITED EDITION       ")
print("")
print("========================================")

input("Press Enter to begin.\n")

print("It's the 1800s and you are getting ready to go on the Oregon Trail")
print("You can bring up to 4 people with you. Who do you bring?")

while numberOfPeople < 4 and done ==False:
    numberOfPeople +=1
    print("\nEnter the name of party member # " + str(numberOfPeople))
    partyMembers.append( input(str(numberOfPeople) + ": "))

    if numberOfPeople <4:
        raw = input("Do you want to add more members? Type 'yes' or 'no':")
        if raw == "no":
            done = True
        else:
            done = False

print("\nGreat! The party members are: ")
for i in partyMembers:
    print(i)
