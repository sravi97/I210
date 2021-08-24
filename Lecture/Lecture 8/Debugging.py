s = input("Please enter a string: ")

for thing in range(len(s)):
    print("Current letter: ", s[thing])
    if thing != len(s) - 1:
        print("Next letter: ", s[thing + 1])
    else:
        print("Next letter: None")



