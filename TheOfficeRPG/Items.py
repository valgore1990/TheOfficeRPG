__author__ = 'joshbrown1'
import random

class Weapon():
    """Base weapon class"""
    def __init__(self, Name, Equipped, To_Hit_Bonus, Damage, Damage_Bonus, Critical_Range):
        self.Name = Name
        self.Equipped = Equipped
        self.To_Hit_Bonus = To_Hit_Bonus
        self.Damage = Damage
        self.Damage_Bonus = Damage_Bonus
        self.Critical_Range = Critical_Range

    def get_damage(self, modifier):
        damage = 0
        for dice in range(self.Damage[0]):
            damage += (random.randint(1, self.Damage[1]) + modifier)
        return damage

    def attack(self):
        return "%d%s%d" % (self.Damage[0], "d", self.Damage[1])

    def __str__(self):
        return "{}\n=====\nTo Hit Bonus = {}\nDamage = {}\nDamage Bonus = {}".format(self.Name, self.To_Hit_Bonus, self.Damage, self.Damage_Bonus)

class Fist(Weapon): #RIGHT
    def __init__(self):
        super(Fist, self).__init__("Fist", False, 2, (1,4), 3, 20)

class Night_Stick(Weapon):
    def __init__(self):
        super(Night_Stick, self).__init__("Night Stick", False, 3, (1,6), 2, 19)

class Dundie(Weapon):
    def __init__(self):
        super(Dundie, self).__init__("Dundie", False, 3, (1,6), 2, 19)

class Ice_Skate(Weapon):
    def __init__(self):
        super(Ice_Skate, self).__init__("Ice Skate", False, 3, (1,6), 2, 19)

class Fun_Jeans(Weapon):
    def __init__(self):
        super(Fun_Jeans, self).__init__("Fun Jeans", False, 3, (1,12), 2, 19)

