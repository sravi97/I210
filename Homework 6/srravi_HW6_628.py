def translate(phrase):
    #words in the dictionary
    wordsDict = {"hello": "hola", "bye": "adios"}
    #store the output
    output = ""
    #splits the dictionary into seperate words
    phrases = phrase.split(" ")
    for word in phrases:
        #if the word is in the dictionary print the "definition"
        if word in wordsDict:
            output+=wordsDict[word] + " "
        #otherwise print three dashes
        else:
            output+= "___"
    return output

print(translate(input("Enter a phrase to be translated: ")))
