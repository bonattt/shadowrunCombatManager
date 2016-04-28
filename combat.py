"""
Johnson's Little Helper Version 1.0
Created by Thomas Bonatti
April 2016
"""

from random import randint
from console import ConsoleCommandException


def build_combat_from_json_list(json_list):

    cmbt = Combat()
    for sub_list in json_list:
        cmbt.add(sub_list[0], sub_list[1], sub_list[2])
    return cmbt


class Combat():

    def __init__(self):
        self.combatants = []

    def contains_name(self, name):
        for current in self.combatants:
            if current.name == name:
                return True

        return False

    def add(self, name, base_init, init_dice):
        if self.contains_name(name):
            raise ConsoleCommandException(name + " already exists in your combat!")
        else:
            self.combatants.append(Combatant(name, base_init, init_dice))
            self.sort_by_init()

    def next(self):

        last = self.get_next_combatant()
        self.combatants.remove(last)
        self.combatants.append(last)
        if (last.init == self.combatants[0].init) and not self.combatants[0].has_acted:
            return_val = [last] + self.next()
        else:
            return_val = [last]

        last.change_init(-10)
        last.has_acted = True

        if self.turn_over():
            self.new_turn()
        elif self.init_pass_over():
            self.next_init_pass()

        return return_val

    def get_next_combatant(self):
        if len(self.combatants) == 0:
            raise ConsoleCommandException("no combatants in combat")

        for combatant in self.combatants:
            if not combatant.has_acted:
                return combatant
        raise Exception("should not exit the for-each loop without returning," +
                        " something went wrong:\n\t Combat.get_next_combatant")

    def turn_over(self):
        for combatant in self.combatants:
            if combatant.init != 0:
                return False
        return True

    def new_turn(self):
        print("--- new turn!! ---")
        self.reroll_init()
        self.next_init_pass()

    def reroll_init(self):
        for current in self.combatants:
            current.roll_init()
        self.sort_by_init()

    def init_pass_over(self):
        for combatant in self.combatants:
            if not combatant.has_acted:
                return False
        return True

    def next_init_pass(self):
        print("--- new init pass! ---")
        for combatant in self.combatants:
            if combatant.init > 0:
                combatant.has_acted = False

    def reduce_init(self, name, init):
        target = self.get(name)
        target.change_init(-init)

    def get_current(self):
        return self.combatants[0]

    def get(self, name):
        for current in self.combatants:
            if current.name == name:
                return current

    def remove(self, name):
        self.combatants.remove(self.get(name))

    def sort_by_init(self):
        combatant_buffer = self.combatants
        self.combatants = []
        while len(combatant_buffer) > 0:
            fastest = get_fastest(combatant_buffer)
            combatant_buffer.remove(fastest)
            self.combatants.append(fastest)

    def as_list(self):
        ls = []
        for combatant in self.combatants:
            ls.append(combatant.as_list())
        return ls


def get_fastest(ls_combantants):
    fastest = ls_combantants[0]
    for combatant in ls_combantants:
        if combatant.init > fastest.init:
            fastest = combatant
    return fastest


class Combatant():

    def __init__(self, name, init, dice):
        self.name = name
        self.init_bonus = int(init)
        self.init_dice = int(dice)
        self.init = 0
        self.roll_init()
        self.damage = 0
        self.stun = 0
        self.has_acted = False

    def roll_init(self):
        self.init = self.init_bonus
        for k in range(self.init_dice):
            self.init += randint(1, 6)

    def get_init(self):
        return self.init

    def as_list(self):
        return [self.name, self.init_bonus, self.init_dice]

    def get_str(self):
        if self.damage > 0 and self.stun == 0:
            return self.get_base_name_str() + "(damage: " + str(self.damage) + ")"
        elif self.damage == 0 and self.stun > 0:
            return self.get_base_name_str() + "(stun: " + str(self.stun) + ")"
        elif self.damage == 0 and self.stun == 0:
            return self.get_base_name_str()
        else:
            return self.get_base_name_str() + "(damage: " + str(self.damage) + ", stun: " + str(self.stun) + ")"

    def get_base_name_str (self):
        if self.has_acted:
            return "- [" + str(self.init) + "] " + self.name
        return "+ [" + str(self.init) + "] " + self.name

    def change_init(self, change):
        self.init = max(self.init + change, 0)

    def change_damage(self, change):
        self.damage = max(self.damage + change, 0)

    def change_stun(self, change):
        self.stun = max(self.stun + change, 0)

    def __str__(self):
        return self.get_str()
