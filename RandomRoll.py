import random
import time

min = int(input("Min: "))
max = int(input("Max: "))

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices......")
    time.sleep(0.65)
    print("The wining number is: ", end=''),
    print(random.randint(min, max))

    roll_again = input("roll the dices again? [y or n] ")

if roll_again == "no" or roll_again == "n":
    print("Thanks for testing...")