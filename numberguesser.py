import random
import math

#take user input
low = int(input("Enter lower number: "))
high = int(input("Enter higher number: "))

#create random number between inputs
x = random.randint(low, high)

#tell user number of guesses allowed
print("You have", round(math.log(high - low + 1, 2)), "guesses.")

count = 0
while count < math.log(high - low + 1, 2):
    count += 1

    #accept user input as guess
    guess = int(input("Guess a number: "))

    #check user input if correct
    if x == guess:
        print("That is correct!")
        break
    elif x > guess:
        print("That is too low!")
    elif x < guess:
        print("That is too high!")

#notify user number of turns ran out
if count > math.log(high - low + 1, 2):
    print("Sorry, the number was %d" % x + "!")