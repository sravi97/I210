#define function
def reverse(phonebook):
    #creating the dictionary
    reversePhonebook = {}

    #for loop that loops for all the key-value pairs 
    for key in phonebook:
        #gets the value from the current key
        newKey = phonebook[key]
        #define the value as new key and assign the old key as new value
        reversePhonebook[newKey] = key
    #returns reversed phone book
    return reversePhonebook

#main
print(reverse(phonebook = {'Smith, Jane':'123-45-67', 'Doe, John': '987-65-43',
                           'Baker,David':'567-89-01'}))
    
