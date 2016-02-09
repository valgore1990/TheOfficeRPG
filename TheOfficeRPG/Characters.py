__author__ = 'joshbrown1'
import Items
import random
import time


class Entity():
    def __init__(self,Name, Armor_Class, Hit_Point, Initiative):
        self.Name = Name
        self.Hit_Points = Hit_Point
        self.Armor_Class = Armor_Class
        self.Initiative = Initiative
        #self.Offense = Offense
        #self.Inventory = Inventory

    def is_dead(self):
        return self.Hit_Points <= 0

    def get_name(self):
        return self.Name

    def get_armor_class(self):
        return self.Armor_Class

    def get_hit_points(self):
        return self.Hit_Points




class Player(Entity):
    def __init__(self, Name, Armor_Class, Hit_Point, Initiative, Offense, Inventory):
        super(Player, self).__init__(Name, Armor_Class, Hit_Point, Initiative)
        self.Offense = Offense
        self.Inventory = Inventory


    def who_starts_attack(self, player, enemy):
        print("You run into %s" % enemy.Name)
        while True:
            if (player.Initiative + random.randint(0, 20) < (enemy.Initiative + random.randint(0,20))):
                return player.Name
            elif (player.Initiative + random.randint(0, 20) > (enemy.Initiative + random.randint(0,20))):
                return enemy.Name


    def is_critical(self, crit_range, roll):
        if (roll >= crit_range):
            return True
        else:
            return False

    def attack(self, attacker, defender, attack_type):
        initial_roll = (random.randint(1,20))
        to_hit_roll = (initial_roll + attacker.Offense.To_Hit_Bonus)
        crit = self.is_critical(attacker.Offense.Critical_Range, initial_roll)
        if to_hit_roll < defender.Armor_Class and crit != True:
            print("%s's Armor Class is too high" % defender.Name)
            time.sleep(1)
            return defender.Name
        multiplier = 1
        if attack_type.lower() == "power attack":
            if random.randint(1,4) == 1 and crit != True:
                print("%s tried to power attack %s, but you missed" % (attacker.Name,defender.Name))
                time.sleep(1)
                return defender.Name
            multiplier = 2*multiplier
        if crit:
            multiplier = multiplier*2
        damage_dealt = (attacker.Offense.get_damage(attacker.Offense.Damage_Bonus)*multiplier)
        if crit:
            print("%s critically hit %s for %d damage" % (attacker.Name, defender.Name, damage_dealt))
            time.sleep(1)
        else:
            print("%s hit %s for %d damage" % (attacker.Name, defender.Name, damage_dealt))
            time.sleep(1)
        defender.Hit_Points -= damage_dealt
        print("%s has %d hit points left!" % (defender.Name, defender.Hit_Points))
        time.sleep(1)
        return defender.Name

    def begin_attack(self, player, enemy):
            start = self.who_starts_attack(player,enemy)
            print("%s goes first" % start)
            time.sleep(1)
            #print("%s has %d Armor Class\n%s has %d Armor Class" % (player.Name, player.Armor_Class, enemy.Name, enemy.Armor_Class))
            actions = ("attack", "power attack")
            while True:
                if start == player.Name:
                    selection = input(("Please select an action: %s or %s\n>") % (actions[0], actions[1]))
                    if selection.lower() != actions[0] and selection.lower() != actions[1]:
                        print("Please select a valid input\n>")
                    else:
                       start = self.attack(player, enemy, selection.lower())
                elif start == enemy.Name:
                    start = self.attack(enemy, player, "attack")
                if player.is_dead():
                    print("You ded")
                    return
                if enemy.is_dead():
                    print("he dedd")
                    return


    def get_offense(self):
        return self.Offense

    def get_inventory(self):
        return self.Inventory



class Enemy(Entity):
    def __init__(self, Name, Armor_Class, Hit_Point, Initiative, Offense, Inventory):
        super(Enemy, self).__init__(Name, Armor_Class, Hit_Point, Initiative)
        self.Offense = Offense
        self.Inventory = Inventory


    def get_offense(self):
        return self.Offense

    def get_inventory(self):
        return self.Inventory
