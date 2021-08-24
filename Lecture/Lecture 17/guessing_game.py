import random

print("\tWelcome to 'Guess my Number'!")
print()
print("I'm thinking of a number between 1 and 100. Try to guess it in as few attempts as possible.\n")

number = random.randrange(1,101)
count = 0
while number:
    guess = eval(input("Take a guess: "))
    count += 1
    if guess < number:
        print ("Higher...")
    elif guess > number:
        print ("Lower...")
    else: guess == number:
        print("You guessed it! The number was", number, "and it only took you", count, "number of tries.")
        break

