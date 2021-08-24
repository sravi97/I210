import donation

# main

# Section 1 - get all of the donations and output the values

# As an example of how to get an amount, this gets 1 donation and prints it out
# Run the program a few times and notice that the amount changes.
# If the code won't run, did you put this file and donation.py in the same directory?

def get_amounts(num):
    amount = []

    for i in range(num):
        amount.append(donation.get_donation())
        
    return (amount)

my_amounts = get_amounts(200)
print("The donations amounts:", my_amounts)
print("The donations in order:", sorted(my_amounts))

# Section 2 - Compute basic categories
small = 0
medium = 0
large = 0
for donation in my_amounts:
    #if we have a 1, 2,3,4 or 5 we want to add 1 to the small donation tally
    if donation in (1,2,3,4,5):
        small += 1
    #if we have a 6-15 we want to add 1 to the medium donation tally
    elif donation >= 6 and donation <= 15:
        medium += 1
    elif donation >= 16:
        large += 1
        

print("There were", num_amounts(small), "small donations ($5 or less).")
print("There were", medium, "medium donations ($6-$15).")
print("There were", large, "large donations ($16 or more).")
            

# Section 3 - Compute success or failure
total = sum(my_amounts)
print("The total amount of money raised is:", total)
year = 2018
if total >= year:
    print("The fundraising goal was met.")
else:
    print("The fundraising goal was not met.")

# Section 4 - What can you expect from the bank?
print("The bank cashed this amount out as:")
#number of 100s
print("100s:", total//100)
#number of 20s
print("20s:", (total % 100)//20)
#number of 10s
print("10s:", ((total % 100)%20)//10)
#number of 5s
print("5s:", (((total % 100)%20)%10)//5)
#number of 1s
print("1s:", ((((total % 100)%20)%10)%5)//1)
