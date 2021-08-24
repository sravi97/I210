def mirror(string):
    #letters that have mirrors
    letters = {'b':'d','d':'b','o':'o','p':'q','q':'p','v':'v','w':'w','x':'x'}
    #initialize the output string
    output=''
    #checking the chararcters in the strings
    for char in string:
        #if the character is present, take its mirror and append to output
        if char in letters.keys():
            output=output+letters[char]
        #if the character isn't in the letter dictionary, print INVALID
        else:
            return 'INVALID'
    #prints the mirror of output
    return output[::-1]

print(mirror("vow"))
print(mirror("wood"))
print(mirror("bed"))

