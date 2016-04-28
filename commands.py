import sys
import json
import os.path
from dis import code_info
from random import randint
from combat import Combat
from console import ConsoleCommandException
from combat import build_combat_from_json_list


class RollCommand():

    def __init__(self):
        pass

    def help(self):
        print("\troll [dice pool] [optional: limit]")
        print("This command rolls a number of dice equal to "
              "the dice pool, then displays the result.")

    def execute(self, args):
        if len(args) == 1:
            roll(int(args[0]))
        elif len(args) == 2:
            limited_roll(int(args[0]), int(args[1]))
        else:
            print("roll [dice pool] [limit (default = 9223372036854775807)]")
            print("makes a roll with the given dice pool and limit")


class AboutCommand():

    def __init__(self):
        pass

    def help(self):
        print_about_statement()

    def execute(self, args):
        print_about_statement()


def print_about_statement():
    print("Johnson's Little Helper version 1.0")
    print("Johnson's Little Helper was produced by Thomas Bonatti")
    print("This software may be freely used, distributed, and modified by anyone, it is 100% open source.")
    print("This software is intended to be used to an aid for managing in the tabletop RPG Shadowrun, 5th ed.,"
          " by Catalyst Game Labs.")


class NewCombat():

    def __init__(self, console):
        self.console = console

    def help(self):
        print("\tnew:\nThis command launches a new empty combat."
              "If there is already a combat running, this command"
              " asks before overwriting it.")

    def execute(self, args):
        if len(args) != 0:
            print("new-combat takes no args")
            print("new combat creates a new (empty) combat instance, overwriting the current combat")
        else:
            print("initiated a new combat")
            self.new_combat()

    def new_combat(self):
        if self.console.combat is None:
            self.console.combat = Combat()
        elif confirm("you have an active combat. Would you like to overwrite it with a new one? [y/n]"):
            self.console.combat = Combat()


class AddCombatant():

    def __init__(self, console):
        self.console = console

    def help(self):
        print("\tadd [name] [base init] [init dice]:\nAdds a new combatant with" +
              " the given name, base initiative, and initiative dice." +
              "Names must be unique.")

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

    def help(self):
        print("\tview\nDisplays the current initiative order without changing it.")

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

    def help(self):
        print("\tremove-combatant [name]:\nremoves the selected combatant from the turn order.")

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

    def help(self):
        print("\tnext:\ndisplays the next combatant(s) to take their turn(s) and displays the initiative order.")

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

    def help(self):
        print("\tdamage [name] [amount]:\ndeals the specified amount of damage from the target combatant")

    def execute(self, args):
        if self.console is None:
            raise ConsoleCommandException("there is no active combat")

        if len(args) != 2:
            raise ConsoleCommandException("damage [name] [damage]")

        combatant = self.console.combat.get(args[0])
        combatant.change_damage(int(args[1]))


class HealCommand():

    def __init__(self, console):
        self.console = console

    def help(self):
        print("\theal [name] [amount]:\nheals the specified amount of damage from the target combatant")

    def execute(self, args):
        if self.console.combat is None:
            raise ConsoleCommandException("there is no active combat")

        if len(args) != 2:
            raise ConsoleCommandException("heal [name] [damage]")

        combatant = self.console.combat.get(args[0])
        combatant.change_damage(-int(args[1]))


class StunCommand():

    def __init__(self, console):
        self.console = console

    def help(self):
        print("\tstun [name] [amount]:\ndeals the specified amount of stun-damage from the target combatant")

    def execute(self, args):
        if self.console.combat is None:
            raise ConsoleCommandException("there is no active combat")

        if len(args) != 2:
            raise ConsoleCommandException("heal [name] [damage]")

        combatant = self.console.combat.get(args[0])
        combatant.change_stun(int(args[1]))


class HealStunCommand():

    def __init__(self, console):
        self.console = console

    def help(self):
        print("\tstun-heal [name] [amount]:\nheals the specified amount of stun-damage from the target combatant")

    def execute(self, args):
        if self.console.combat is None:
            raise ConsoleCommandException("there is no active combat")

        if len(args) != 2:
            raise ConsoleCommandException("heal [name] [damage]")

        combatant = self.console.combat.get(args[0])
        combatant.change_stun(-int(args[1]))



class ResetInitCommand():

    def __init__(self, console):
        self.console = console

    def help(self):
        print("\treset-init:\nthis rerolls immediately starts a new combat turn")

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

    def help(self):
        print("\tclear:\nclears the console screen")

    def execute(self, args):
        print("\n"*50)


class RemoveCombatant():

    def __init__(self, console):
        self.console = console

    def help(self):
        print("\tremove-combatant [name]:\nthis command removes the named combatant from the combat")

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

    def help(self):
        print("\tsave [save name]:\nsaves the current game to the current name. If the name is already used" +
              " this will ask before overwriting it. Save names cannot include spaces.")

    def execute(self, args):
        if self.console.combat is None:
            raise ConsoleCommandException("there is no active combat")

        if len(args) != 1:
            raise ConsoleCommandException("save [save name]")
        try:
            self.__saveFile__(args[0])
            print("successfully saved \"" + args[0] + "\"")
        except IOError as e:
            raise ConsoleCommandException("\tsave failed\nIOError: \"" + str(e) + "\"")
        except Exception as e:
            raise e
            # raise ConsoleCommandException("\tsave failed\nunknown error: \"" + str(e) +"\"")

    def __saveFile__(self, save_name):
        save_path = "save_files/" + save_name + ".json"
        outfile = open(save_path, "w")
        if os.path.isfile(save_path):
            if not confirm("This save name is already used, would you like to overwrite it? [y/n]"):
                raise ConsoleCommandException("game not saved.")
        json.dump(self.console.combat.as_list(), outfile)


class LoadCommand():

    def __init__(self, console):
        self.console = console

    def help(self):
        print("\tload [save name]:\nloads a previously saved game. If a game is currently loaded," +
              " this will ask before overwriting it. Save names cannot include spaces.")

    def execute(self, args):
        if len(args) != 1:
            raise ConsoleCommandException("load [save name]. Please note, save names cannot contain spaces." +
                                          " Try using \"_\" or \"-\" instead ")

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


class HelpCommand():

    def __init__(self, console):
        self.console = console

    def help(self):
        print("\thelp\nPrints a list of availible commands")
        print("\thelp [command]:\nGives instructions for the use of the selected command.")

    def execute(self, args):
        if len(args) == 0:
            print("available commands")
            for command in self.console.commands:
                print(command)

        elif len(args) == 1:
            if args[0] in self.console.commands:
                self.console.commands[args[0]].help()
            else:
                raise ConsoleCommandException("help: command not found")


        else:
            raise ConsoleCommandException("help [command] for info on specific command")


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

