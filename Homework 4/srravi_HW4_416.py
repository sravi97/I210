#get input from user
first = input("Enter first word: ")
second = input("Enter second word: ")
third = input("Enter third word: ")

#print True if words were entered in dictionary order
if first <= second <= third:
    print(True)
