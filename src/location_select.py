import time
from story import ironforge_story

def player_location():
    loc_1 = "Ironforge"
    loc_2 = "Norwich"
    loc_3 = "Beckton"
        
    print("1. ", loc_1)
    time.sleep(.5)
    print("2. ", loc_2)
    time.sleep(.5)
    print("3. ", loc_3)
    time.sleep(.5)
    choice = input("Chose Your Location: ")

    if choice == "1":
        print("Your chosen Location is a Blacksmith town,",
                "all weapons get created here.")
        ironforge_story.weapon_pick()

    elif choice == "2":
        print("Your chosen location is a peaceful town,",
                "all people are nice here.")

    elif choice == "3":
        print("Your chosen location is a rough and violent village,",
                "well known for monster attacks, so they're very defensive.")

    else:
        print("chose a location listed!!!")
        time.sleep(.5)
        player_location()
