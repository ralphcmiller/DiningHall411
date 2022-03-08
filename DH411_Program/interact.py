# Proof of concept for the dining hall 411 text program
from dbsetup import CreateMenuDB, addMenuItem, findMenuItem

print("Welcome to Dining Hall 411!")

response = input("""Please respond with the following options:
-Location <RachelCarson, PorterKresge, CrownMerrill, CowellStevenson, College910>
-Date <dd/mm/yy>
-Food <Name of Specific Meal> **Can be left blank to receive full menu for specified date**\n""")

#storing response in lowercase, splitting at options
response = response.lower()
splitone = response.split("-")

#storing location, date, food in temp variables
location = None
date = None
food = None

#remove argument from input
for i in splitone:
    if "location" in i:
        temp = i.split(" ", 1)
        location = temp[-1]
        #if there is a space in location, remove it
        if " " in location:
            location = location.replace(" ", "")
    if "date" in i:
        temp = i.split(" ", 1)
        date = temp[-1]
    if "food" in i:
        temp = i.split(" ", 1)
        food = temp[-1]

#Query Database
query = findMenuItem(location, date, food)

#clean query and respond
#if a specific food is specified print a single message with where it is
#otherwise, loop through all the menu items for the requested date, and
#print the meal time (lunch, dinner, etc) followed by the food name.
if food:
    for i in query:
        print("{} is at {} on {}".format(i[0],i[1],i[2])
else:
    temp = query[0]
    temp = temp[1]
    print("The menu for the {} location is:".format(temp)
    for i in query:
        print("{}: {}".format(i[3], i[2])


