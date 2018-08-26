import os
import time
import location_select

def main():
    print("Load Exsisting Account")
    time.sleep(.5)
    print("or")
    time.sleep(.5)
    print("Create New Account")
    choice = input("What do you want to do: ")

    if choice == "1":
        pass
    elif choice == "2":
        username = input("Enter your username: ")
        time.sleep(0.5)
        os.system("cls")
        print("Hello", username, "please chose your location")
        location_select.player_location()
