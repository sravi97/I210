#get input from user
sentence = input("Enter a sentence: ")
total = 0
def average():
#splits sentence
    words = sentence.split()
    for word in words:
        total += len(word)
    return (total*1/len(list))
print(total/len(list))


