#define vowels
vowels = "aeiouAEIOU"
def exclamation(string):
#if there's a vowel, replace it with four consecutive vowels
    for letter in vowels:
        string = string.replace(letter, letter*4)
#print the result and add an exclamation at the end
    return (string + "!")

print(exclamation("argh"))
print(exclamation("hello"))
