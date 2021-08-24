def lastfirst(string):
#list of last names
    LastNames = []
#list of last names
    FirstNames = []
    for word in string:
#split the names at the comma
        split = word.split(",")
#appends whatever is in the 0 index position to the LastNames list
        LastNames.append(split[0])
#appends whatever is in the 1 index position to the FirstNames list
        FirstNames.append(split[1].strip())
    return (FirstNames, LastNames)

print(lastfirst(["Gerber, Len", "Fox, Kate", "Dunn, Bob"]))
