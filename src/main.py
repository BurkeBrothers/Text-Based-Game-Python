import account_creation
import time

def menu():
    print("Welcome to my game", "\n" * 2)
    time.sleep(.5)
    print("Start")
    time.sleep(.5)
    print("Exit")
    time.sleep(.5)
    choice = input("Choice: ")

    if choice == "1":
        account_creation.main()
    elif choice == "2":
        quit()

menu()