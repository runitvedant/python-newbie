import random
# computers choice
choice1 = random.randint(0,100)
while True:

    my_choice = int(input("my prediction:"))
    if my_choice > choice1:
        print("Go low")

    elif my_choice < choice1:
        print("Go high")

    else:
        print("Correct")
        break
