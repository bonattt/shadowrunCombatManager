
class Console():

    DEFAULT_MSG = "combat-mgr"

    def __init__(self):
        self.combat = None
        self.commands = {}

    def run_console(self):
        while True:
            choices = (str(input(self.DEFAULT_MSG + "> "))).split(" ")
            print()
            if choices[0].lower() == "exit":
                return
            if choices[0] in self.commands:
                self.handle_choice(choices)
            else:
                print("command not found")
            print()

    def handle_choice(self, choices):
        command = self.commands[choices[0]]
        args = choices[1:]
        try:
            command.execute(args)
        except ConsoleCommandException as e:
            print(e.msg)


class ConsoleCommandException(Exception):

    def __init__(self, msg):
        self.msg = msg