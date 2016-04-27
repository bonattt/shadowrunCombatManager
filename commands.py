import sys
import json
from dis import code_info
from random import randint
from combat import Combat
from console import ConsoleCommandException
from combat import build_combat_from_json_list


class RollCommand():

    def __init__(self):
        pass

    def execute(self, args):
        if len(args) == 1:
            roll(int(args[0]))
        elif len(args) == 2:
            limited_roll(int(args[0]), int(args[1]))
        else:
            print("roll [dice pool] [limit (default = 9223372036854775807)]")
            print("makes a roll with the given dice pool and limit")


class NewCombat():

    def __init__(self, console):
        self.console = console

    def execute(self, args):
        if len(args) != 0:
            print("new-combat takes no args")
            print("new combat creates a new (empty) combat instance, overwriting the current combat")
        else:
            print("initiated a new combat")
            self.new_combat()

    def new_combat(self):
        if self.console.combat == None:
            self.console.combat = Combat()
        elif confirm("you have an active combat. Would you like to overwrite it with a new one? [y/n]"):
            self.console.combat = Combat()


class AddCombatant():

    def __init__(self, console):
        self.console = console

    def execute(self, args):
        if len(args) != 3:
            print("add [name] [base init] [init dice]")
            print("add adds a new combatant to your active combat")
        else:
            if self.console.combat == None:
                print("there is no active combat to add combatants to")
            else:
                self.console.combat.add(args[0], args[1], args[2])
                print("added " + args[0] + " to the initiative order")


class ViewCommand():

    def __init__(self, console):
        self.console = console

    def execute(self, arg):
        view_combatants(self.console)


def view_combatants(console):
    if console.combat == None:
        print("there is no active combat to view")
    elif len(console.combat.combatants) == 0:
        print("the combat is empty")
    else:
        for combatant in console.combat.combatants:
            print(combatant)


class RemoveCombatant():

    def __init__(self, console):
        self.console = console

    def execute(self, args):
        if len(args) != 1:
            raise ConsoleCommandException("remove [combatant name]")

        if self.console.combat is None:
            raise ConsoleCommandException("there is no active combat")

        if args[0] in self.console.combat.combatants:
            print("removed " + args[0] + " from the combat")
            self.console.combat.remove(args[0])

class NextCombatant():

    def __init__(self, console):
        self.console = console

    def execute(self, args):
        if self.console.combat is None:
            raise ConsoleCommandException("there is no active combat")

        if len(args) != 0:
            raise ConsoleCommandException("next takes no args")

        next_turn = self.console.combat.next()
        msg = "Turn: "
        for combatant in next_turn:
            msg += combatant.name + " "
        print(msg)
        view_combatants(self.console)


class DamageCombatant():

    def __init__(self, console):
        self.console = console

    def execute(self, args):
        if self.console is None:
            raise ConsoleCommandException("there is no active combat")

        if len(args) != 2:
            raise ConsoleCommandException("damage [name] [damage]")

        combatant = self.console.combat.get(args[0])
        combatant.damage += int(args[1])


class HealCommand():

    def __init__(self, console):
        self.console = console

    def execute(self, args):
        if self.console.combat is None:
            raise ConsoleCommandException("there is no active combat")

        if len(args) != 2:
            raise ConsoleCommandException("heal [name] [damage]")

        combatant = self.console.combat.get(args[0])
        combatant.damage -= int(args[1])


class ResetInitCommand():

    def __init__(self, console):
        self.console = console

    def execute(self, args):
        if self.console.combat is None:
            raise ConsoleCommandException("there is no active combat")

        if len(args) != 0:
            raise ConsoleCommandException("reset-init has no arguments")

        self.console.combat.reroll_init()
        print("reset the initiative order")


class ClearCommand():

    def __init__(self):
        pass

    def execute(self, args):
        print("\n"*21)


class RemoveCombatant():

    def __init__(self, console):
        self.console = console

    def execute(self, args):
        if self.console.combat is None:
            raise ConsoleCommandException("there is no active combat")

        if len(args) != 1:
            raise ConsoleCommandException("remove [combatant name]")

        self.console.combat.remove(args[0])
        print("removed", args[0], "from the combat")


class SaveCommand():

    def __init__(self, console):
        self.console = console

    def execute(self, args):
        if self.console.combat is None:
            raise ConsoleCommandException("there is no active combat")

        if len(args) != 1:
            raise ConsoleCommandException("save [save name]")
        try:
            with open("save_files/" + args[0] + ".json", "w") as outfile:
                json.dumps(self.console.combat.as_list(), outfile)
        except Exception:
            raise ConsoleCommandException("save failed: unknown error")

        print("successfully saved \"" + args[0] + "\"")


class LoadCommand():

    def __init__(self, console):
        self.console = console

    def execute(self, args):
        if len(args) != 1:
            raise ConsoleCommandException("load [file name]")

        if self.console.combat is not None:
            if not confirm("Loading a new combat will overwrite your current combat. Is that okay? [y/n]"):
                return
        try:
            with open("save_files/" + args[0] + ".json", "r") as file:
                data = json.load(file)
                verify_json_data(data)
                self.console.combat = build_combat_from_json_list(data)
        except ConsoleCommandException as e:
            raise e
        except Exception:
            raise ConsoleCommandException("load file failed: unknown error")
        print("successfully loaded \"" + args[0] + "\"")


def verify_json_data(json_data):
    try:
        for sub_list in json_data:
            int(sub_list[1])
            int(sub_list[2])
            if len(sub_list) > 3:
                raise Exception()
    except Exception:
        raise ConsoleCommandException("load file failed: json data in unexpected form")


def confirm(msg):
    choice = str(input(msg))
    if choice.startswith("y"):
        return True
    return False


def roll(dice_pool):
    limited_roll(dice_pool, sys.maxsize)


def limited_roll(dice_pool, limit):
    rolls = []
    ones = 0
    hits = 0
    for k in range(dice_pool):
        roll = randint(1, 6)
        if roll == 1:
            ones += 1
        elif roll >= 5:
            hits += 1
        rolls.append(roll)
    if hits > limit:
        print("hit limit!")
        hits = limit
    print_roll(rolls, ones, hits, dice_pool)

def print_roll(rolls, ones, hits, dice_pool):
    if ones > int(dice_pool / 2):
        if hits == 0:
            print("CRITICAL GLITCH")
        else:
            print("GLITCH!")
    print(rolls)
    print("hits: ", hits, "ones: ", ones, "sum:", sum(rolls))

