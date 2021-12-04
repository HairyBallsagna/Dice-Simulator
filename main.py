import random
from art import art

while True:
    direction = input("Press enter to roll or exit to quit the program: ")
    if direction == "exit":
        print("\nExiting")
        break
    num = random.randint(1, 6)
    print(art[num - 1])