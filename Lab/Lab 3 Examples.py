##print("What would you like to do this weekend?")
##
##choice = input("Do you want to go to the park or to a movie?")
##if choice == "park" or choice == "movie":
##    if choice == "park":
##        print("Great! Let's go!")
##    else:
##        movie = input("Is it true that we have enough money for tickets? [True, False]")
##        if movie == "True" or movie == "False":
##            if movie == "True":
##                print("Excellent! Bring on the popcorn!")
##            else:
##                print("That's ok. It's a nice day for the park.")
##        else:
##            print("not valid answer")
##
##else:
##    print("That's not something we can do this weekend.")


num_list = eval(input("Please enter a list of numbers [x,y,z,etc.]: "))
print("The largest number in your list is:", max(num_list))
print("The smallest number in your list is:", min(num_list))
answer = input("Would you like to add a number or remove one?")
if answer == "add" or answer == "remove":
    if answer == "add":
        new = eval(input("What is the new number?"))
        print(int((num_list.append(new))))
