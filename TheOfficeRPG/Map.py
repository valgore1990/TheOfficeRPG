__author__ = 'joshbrown1'
from Items import Dundie, Ice_Skate, Fun_Jeans, Fist, Night_Stick
from Characters import Enemy

class Base_Room():
    def __init__(self, name, description, Enemy_y_n, actions):
        self.Name = name
        self.Description = description
        self.Enemy = Enemy_y_n
        self.paths = {}
        self.Actions = actions

    def look(self, room_description):
        print(room_description)

    def add_paths(self, paths):
        self.paths.update(paths)

    def go(self, direction):
        return self.paths.get(direction, None)

    def create_enemy(self, name, AC, HP, Init, Offense, Inventory):
        enemy = Enemy(name, AC, HP, Init, Offense, Inventory)
        self.Enemy = enemy
        return enemy

    def player_actions(self):
        self.look(self.Description)
        print("You can either:")
        for key in self.Actions:
            print(key)
        selection = input(">:")
        for keys, value in self.Actions.items():
            if keys != selection.lower():
                return
            if keys == selection.lower():
                return value


class Entrance(Base_Room):
    def __init__(self, name, description, Enemy_y_n, actions):
        super(Entrance, self).__init__(name, description, Enemy_y_n, actions)
        #self.Description = "You reach Dunder Mifflin. To the left is the parking lot. In front of you are the doors to the building."
        self.add_paths({"north": "Front_Door", "west": "Parking_Lot"})

class Parking_Lot(Base_Room):
    def __init__(self, name, description, Enemy_y_n, actions):
        super(Parking_Lot, self).__init__(name, description, Enemy_y_n, actions)
        #self.Description = "You reach Dunder Mifflin. To the left is the parking lot. In front of you are the doors to the building."
        self.add_paths({"north": "Michael's Car", "south": "Entrance"})


    #def look, get items, fight, go forward, go back, pick up, use
#Room Dictionaries
Entrances = {
    "Name": "Entrance",
    "Description": "You reach Dunder Mifflin. To the left is the parking lot. In front of you are the doors to the building.",
    "Actions": {"go left": "Parking Lot", "go forward": "Front Door"},
    "Exit": False
}

Parking_Lots = {
    "Name": "Parking Lot",
    "Description": "You look around and see one car. It's Michael's.",
    "Actions": {"search": "Michael's Car", "go back": "Entrance"},
    "Exit": False
}

Search_Michaels_Car = {
    "Name": "Michael's Car",
    "Description": "You find that his car is unlocked.",
    "Actions": {"search": "Items", "go back": "Parking Lot"},
    "Key": "Entrance Key",
    "Items": (Dundie, Fun_Jeans, Ice_Skate),
    "Exit": False
}

Front_Doors = {
    "Name": "Front Door",
    "Description": "This is the front door. It appears to be locked.",
    "Actions": {"unlock door": "Front Room", "go back": "Entrance"},
    "Exit": False
}

Front_Room_Shop = {
    "Name": "Front Room",
    "Description": "The room has an Espresso Bar. Running the Bar is Hank.",
    "Actions": {"Stupid": "Stupid"},
    "Exit": False
}

Warehouse = {
    "Name": 5,
    "Description": 5,
    "Actions": 5,
    "Exit": False
}
