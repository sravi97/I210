#get a message from the user
message = input("Please enter a message: ")
for i in range(len(message)):
    print (message[0:i+1])
