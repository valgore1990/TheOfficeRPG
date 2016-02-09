__author__ = 'joshbrown1'
from Map import Base_Room
from Map import Entrance
from Map import Parking_Lot
from Map import Search_Michaels_Car
from Map import Front_Doors
from Map import Front_Room_Shop
from Characters import Player
from Characters import Enemy
from Items import Fist
from Items import Night_Stick
from Items import Fun_Jeans
import random

#map = dict ( (item['Name'],item) for item in (Entrance, Parking_Lot, Search_Michaels_Car, Front_Doors, Front_Room_Shop))


def initialize():

    Gauntlet = Fist()
    Guard_Stick = Night_Stick()
    Jeans = Fun_Jeans()

    name = input("What is your name? \n>")
    Main_Character = Player(name, 15, 45, 3, Gauntlet, None)
    Bill = Enemy("Bill", 15, 100, 2, Guard_Stick, None)
    Front = Entrance("Entrance", "you reach dunder", "n",{"go left": "Parking Lot", "go forward": "Front Door"})
    ParkingLot = Parking_Lot("Parking_Lot", "you see Michael's car!", "n", {"north": "Michael's Car", "south": "Entrance"})
    #Main_Character.begin_attack(Main_Character, Bill)
    map = {Front: "Entrance", ParkingLot: "Parking_Lot" }
    return(Main_Character, map)


def game_loop(room, map):
    #maps, character = initialize()
    #print(room['Description'])
    next = None
    while not next:
        None

    # if room['Exit']:
    #     print('\nThank you for playing!')
    #     return
    #
    # next = None
    #
    # while not next:
    #     print("\nHere are your options:")
    #     for item in room['Actions'].keys():
    #         print("\t" + item)
    #
    #     user_input = input("\n>")
    #     user_input = user_input.strip().lower() # just take  lower case for simplicity
    #     if user_input in room['Actions']:
    #         if room['Actions'][user_input] == "Items":
    #             Looting(room)
    #             user_input = "go back"
    #
    #         elif user_input == "unlock door":
    #             flag = Unlock_Door(room)
    #             if flag == True:
    #                 print("Door is unlocked")
    #                 user_input = "unlock door"
    #             else:
    #                 user_input = "go back"
    #         elif user_input == "equip":
    #             Equipping()
    #         next = room['Actions'][user_input]
    #     else:
    #         print("'%s' is not a supported option. Please try again" % user_input)
    # game_loop(map[next], map)

def Looting(current_room):

    if "Key" in current_room:
        print(current_room["Key"], "has been added to your inventory")
        #Josh_Brown["Inventory"]["Key"] = current_room["Key"]

    print("You find these usable weapons:")
    for weapons in current_room["Items"]:
        if current_room["Items"][weapons]["Loaded"] == False:
            print("\t", weapons)
        else:
            print("Nothing")
            return

    print("You can either 'take everything', 'inspect', or 'go back'")
    user_input = input("\n>")

    while True:
        if user_input.lower() == "take everything":
           # Josh_Brown["Inventory"]["Weapons"] = (current_room["Items"])
            for a in current_room["Items"]:
                #current_room["Items"][a]["Quantity"] = 0 #deprecaded
                current_room["Items"][a]["Loaded"] = True
            print("You took everything")
            empty = True
            #Equipping()
            break
        elif user_input.lower() == "inspect":
            for key, x in current_room["Items"]:
                #print("Quantity:", current_room["Items"][x]["Quantity"])
                #print(current_room["Items"][x])
                print("\tTo Hit Bonus:", current_room["Items"][x]["To Hit Bonus"])
                print("\tDamage Bonus:", current_room["Items"][x]["Damage Bonus"])
                Damage = ("\tDamage:", current_room["Items"][x]["Damage"])
                print(Damage[0], Damage[1][0],"d", Damage[1][1])
                print("\tCritical Range:", current_room["Items"][x]["Critical Range"])
            break
        elif user_input.lower() == "go back":
            break
        else:
            print("Please enter a valid option")


def Equipping():
    ()



def Unlock_Door(room):
    ()
    #if "Key" in Josh_Brown["Inventory"]:
 #       keys_in_possession = Josh_Brown["Inventory"]["Key"]
  #      print(keys_in_possession)
   #     return True
    #else:
     #   print("You need to find a key")
      #  return False
#Battle(Josh_Brown, Hank)
game_loop (Entrance, map)