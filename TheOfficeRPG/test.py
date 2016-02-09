__author__ = 'joshbrown1'
import random
import time

def is_critical(self, current_turn):
    to_hit = random.randint(1,20)
    if (to_hit >= current_turn.Offense.Critical_Range):
        print("I crit")
        return True
    else:
        return False

def attack(self, attacker, defender, attack_type):
    roll = (random.randint(1,20) + attacker.Offense.To_Hit_Bonus)
    crit = is_critical(attacker)
    if roll < defender.Armor_Class & crit != True:
        print("%s's Armor Class is too high" % defender.Name)
        return defender.Name
    multiplier = 1
    if attack_type.lower() == "power attack":
        if random.randint(1,4) == 1 & crit != True:
            print("%s tried to power attack %s, but you missed" % (attacker.Name,defender.Name))
            return defender.Name
        multiplier = 2*multiplier
    if crit:
        multiplier = multiplier*2
    print("Multiplier is %d" % multiplier)
    damage_dealt = (attacker.Offense.get_damage(attacker.Offense.Damage_Bonus)*multiplier)
    if crit:
        print("%s critically hit %s for %d damage" % (attacker.Name, defender.Name, damage_dealt))
    else:
        print("%s hit %s for %d damage" % (attacker.Name, defender.Name, damage_dealt))
    defender.Hit_Points -= damage_dealt
    print("%s has %d hit points left!" % (defender.Name, defender.Hit_Points))
    return defender.Name

def begin_attack(self, player, enemy):
        start = self.who_starts_attack(player,enemy)
        print("%s goes first" % start)
        print("%s has %d Armor Class\n%s has %d Armor Class" % (player.Name, player.Armor_Class, enemy.Name, enemy.Armor_Class))
        actions = ("attack", "power attack")
        while True:
            if start == player.Name:
                selection = input(("Please select an action: %s or %s\n>") % (actions[0], actions[1]))
                if selection.lower() != actions[0] or selection.lower() != actions[1]:
                    print("Please select a valid input\n>")
                else:
                    attack(player, enemy, selection.lower())
            elif start == enemy.Name:
                attack(enemy, player, "attack")
