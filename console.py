"""
Johnson's Little Helper Version 1.0
Created by Thomas Bonatti
April 2016
"""

class Console():

    DEFAULT_MSG = "combat-mgr"

    def __init__(self):
        self.combat = None
        self.commands = {}

    def run_console(self):
        while True:
            choices = self.get_input()
            print()
            if choices[0].lower() == "exit":
                return
            if choices[0] in self.commands:
                if self.handle_choice(choices):
                    self.view_combatants()
            else:
                print("command not found")
            print()

    def view_combatants(self):
        if self.combat == None:
            print("there is no active combat to view")
        elif len(self.combat.combatants) == 0:
            print("the combat is empty")
        else:
            print("Current Turn: " + str(self.combat.currentTurn))
            for combatant in self.combat.combatants:
                print(combatant)

    def get_input(self):
        choice = str(input(self.DEFAULT_MSG + "> "))
        choice = choice.strip(" ")
        return choice.split(" ")

    def handle_choice(self, choices):
        command = self.commands[choices[0]]
        args = choices[1:]
        try:
            return command.execute(args)
        except ConsoleCommandException as e:
            print(e.msg)
            return False


class ConsoleCommandException(Exception):

    def __init__(self, msg):
        self.msg = msg