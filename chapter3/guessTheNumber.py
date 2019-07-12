import random

secrectNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20. You have 6 guesses!")

# Ask player to guess six times
for guessesTaken in range(1, 7):
    print("Take a guess:")
    guess = int(input())

    if guess < secrectNumber:
        print("Your guess is too low!\n")
    elif guess > secrectNumber:
        print("Your guess is too high!\n")
    else:
        break

if guess == secrectNumber:
    print("\nGood job! You guessed my number in " + str(guessesTaken) + " guesses!\n")
else:
    print("\nNope. The number i was thinking of was " + str(secrectNumber) + " !\n")
