##def open_file(filename):
##    while True:
##        try:
##            file = open(filename, "r")
##            lines = file.readlines()
##            file.close()
##        except:
##            filename = input("That file doesn't exist.\nTry another file name: ")
##        else:
##            break
##    for i in range(len(file)):
##            file[i] = file[i].strip()
##            return file
##
###main
##data = open_file("notafile.txt")
##print("The contents of the file are:")
##print(data)

#question 4
episodes = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
        episodes[i - 1] = episodes[i]
for i in range(6):
        print(episodes[i], end = " ")


###question 5
##login = {"user":"J", "password":"python"}
##print(login['password'])


###question 6
##A = {1, 2, 3, 4, 5}
##B = {4, 5, 6, 7, 8}
##
##print(A & B)
