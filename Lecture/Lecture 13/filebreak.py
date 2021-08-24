#get a file name from the user
while True:
    file_name = input("Please enter a file name or STOP: ")

    if file_name.upper() == "STOP":
        break
    text_file = open(file_name, "r")
    file_content = len(text_file.readlines())
    text_file.close()
    

    print(file_name, "has", file_content, "number of lines.")

