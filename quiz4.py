###Question 3
##poem = """
##
##   Pick a card
##
##       Focus on the coin
##
##           Magicians ar annoying"""
##
##print (poem)
##
###Question 5
##message = "Hello, World!\n"
##print(message.upper())
##print(message.lower())
##print(message.title())
##print(message.strip())
##print(message.replace("World", "Bloomington"))
##print(message.strip().split(", "))
##print(message.count("e"))
##print(message.count("e"))
##print(message[:5])
##print(message.find("Goodbye"))

###Question 6
##groceries = [["oranges", 3], ["apples", 4], ["carrots", 8], ["tomatoes", 2]]
##print(groceries[3][1])

###Question 7
##month = "February"
##day = "17"
##year = "2017"
##
##date = "Today is the {0}th of {1}. The year is {2}."
##
##print(date.format(day, month, year))

#Question 8
import random
def trickOrTreat(houses, candy = 0):
    for house in range(houses):
        result = random.choice(["trick!", "treat!"])
        print (result)
        if result == "treat!":
            candy += 1
    return candy

print(trickOrTreat(3))
print(trickOrTreat(5, 10))
