import random
print("Welcome, adventurer")
Health = 100
Gold = 0
print("Currently you have:")
print("Health =", Health)
print("Gold =",Gold)
print("ROUND 1")
choice = int(input("You are in a dungeon. Click 1 to turn left or 2 to turn right."))
if choice == 1:
    randomchoice = random.randint(1,3)
    if randomchoice == 1:
        print("you just found 50 gold!")
        Gold = Gold + 50
        print("Your current stats are:")
        print("Health =", Health)
        print("Gold =", Gold)
    elif randomchoice == 2:
        print("You face a goblin and lose 30 health")
        Health = Health - 30
        print("Your current stats are:")
        print("Health =", Health)
        print("Gold =", Gold)
    else:
        print("You found a healing potion!")
        Health = Health + 20
        print("Your current stats are:")
        print("Health =", Health)
        print("Gold =", Gold)
elif choice == 2:
    randomchoice1 = random.randint(1,3)
    if randomchoice1 == 1:
        print("You find 100 Gold coins!")
        Gold = Gold + 100
        print("Your current stats are:")
        print("Gold =", Gold)
        print("Health =", Health)
    elif randomchoice1 == 2:
        print("You discovered a trap and lost 50 health points")
        Health = Health - 50
        print("Your current stats are:")
        print("Health =", Health)
        print("Gold =", Gold)
    else:
        print("You discovered a magic fountain and gained 40 health")
        Health = Health + 40
        print("Your current stats are:")
        print("Health =", Health)
        print("Gold =", Gold)
else:
    print("Invalid choice")
if choice == 1 or 2:
    print("You now face the final boss!")
    choice1 = int(input("Press 1 to fight."))
    if choice1 == 1:
        if Health >= 100 and Gold >= 50:
            print("You win!")
        else:
            print("You lose!")
    else:
        print("You chose to run away")