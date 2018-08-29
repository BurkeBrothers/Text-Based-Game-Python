import random

monsters = {"Red Eye Wolf", "Blightfang", "The Painted Terror Monkey"}

randomMonster = random.choice(list(monsters))
health = 100

print(f"You have stummbled upon a {randomMonster} which has {health} health")

class Player:
    def __init__(self):
        #Initialize here

    def attack(self):
        #Do attack stuff here

class Monster:
    def __init__(self):
        #Initialize here

    def attack(self):
#Do attack stuff here
