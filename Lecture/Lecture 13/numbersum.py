total = 0
while True:
    user_input = input("Please enter a number or STOP: ")
    if user_input == "STOP":
        break
    else:
        total += int(user_input)
    
print("The total sum is", total)
        
