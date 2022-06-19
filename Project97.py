import random
print("Number guessing game")
number = random.randint(1, 9)
chance = 0
print("Guess a number between 1 and 9")
while chance < 5:
    guess = int(input("Guess: "))
    if guess == number:
        print("You guessed it!")
        break
    elif guess > number:
        print("Too high")
    else:
        print("Too low")
    chance += 1
    if chance == 5:
        print("You lost!")
        print("The number was", number)
    else:
        print("You have", 5 - chance, "chances left")
print("Thanks for playing!")
input("Press Enter to exit ")
