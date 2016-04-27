
from console import Console
import commands as cmd

def main():
    start_console()


def start_console():
    print("Welcome to the Shadowrun Combat Manager\n\t- IllumiBonatti")
    console = Console()
    add_default_commands(console)
    console.run_console()

def add_default_commands(console):
    console.commands["roll"] = cmd.RollCommand()
    new_combat = cmd.NewCombat(console)
    console.commands["new"] = new_combat
    console.commands["new-combat"] = new_combat
    console.commands["add"] = cmd.AddCombatant(console)
    console.commands["view"] = cmd.ViewCommand(console)
    console.commands["next"] = cmd.NextCombatant(console)
    console.commands["damage"] = cmd.DamageCombatant(console)
    console.commands["heal"] = cmd.HealCommand(console)
    reset_cmd = cmd.ResetInitCommand(console)
    console.commands["reset"] = reset_cmd
    console.commands["reset-init"] = reset_cmd
    console.commands["clear"] = cmd.ClearCommand()
    console.commands["remove"] = cmd.RemoveCombatant(console)
    console.commands["save"] = cmd.SaveCommand(console)
    console.commands["load"] = cmd.LoadCommand(console)
    console.commands["help"] = cmd.HelpCommand(console)




if __name__ == "__main__":
    main()