def names():
    #dictionary to store the names
    name_list = {}
    #continue loop until empty string is entered
    while True:
        #ask user to input a name
        input_name = input("Enter the next name: ")
        #check if input is empty
        if input_name == "":
            #breaks while loop if empty string is entered
            break
        else:
            #check if the input name is in the dictionary
            if input_name in name_list:
                #increases count by one if it is in dictionary
                name_list[input_name] += 1
            else:
                #if it isn't in the dictionary set value to 1
                name_list[input_name] = 1
    #print statements
    single = "There is {} student named {}."
    plural = "There are {} students named {}."
    

    for name in name_list:
        #if count is greater than 1, print the plural statement
        if name_list[name] > 1:
            print(plural.format(name_list[name], name))
        #if count is v  1, print the single statement
        else:
            print(single.format(name_list[name], name))
            
print(names())
