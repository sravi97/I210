#get a list of names
names = eval(input("Enter list: "))

#print names that start with A through M
for name in names:
    for letters in name:
        if letters[0] in "ABCDEFGHIJKLM":
            print (name)

