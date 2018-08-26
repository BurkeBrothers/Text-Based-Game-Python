from weapon_select import *
#from random import *
#import attack
import time

x = 1

def weapon_pick():
    print("These are your available weapons:")

    for i in range(len(weapons)):
        time.sleep(.5)
        print(f"{i}. {weapons[i]}")

    choice = int(input("What weapon do you want? "))
    inventory.append(weapons[choice])
    print("Weapon added:", weapons[choice])
    time.sleep(x)
    print("\n")
    story_part1()
    pass

def story_part1():
    print(inventory)
    time.sleep(x)
    print("you have arrived at a town known", "for blacksmithing weapons and armour", 
          "although most visitors are'nt welcome to the village, people that buy are.\n")
    time.sleep(x)
    print("You decided to buy a sword and then left the village.\n")
    time.sleep(x)
    print("You came across a 6 foot tall wolf given the alias 'red eye wolf', It was given this name",
          "due to its large red eyes.\n")
    time.sleep(x)
    attack.attackMonster()


#testing
weapon_pick()
story_part1()