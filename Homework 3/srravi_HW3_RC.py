import random
def randomCinema(list):
    #getting the number of movies they'd like to generate
    num = int(input("Please enter a number of movies you'd like to generate: "))
    #display results
    print ("Welcome to Randoplex! Currently playing movies are: ")
    for i in range(num):
        print(random.choice(list) + " " + random.choice(list) + " " + random.choice(list))

#asking user for a list of words
randomCinema(eval(input("Please enter a list of words: ")))





