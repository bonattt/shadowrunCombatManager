"""
Johnson's Little Helper Version 1.0
Created by Thomas Bonatti
April 2016
"""

from console import Console
import commands as cmd


def start_console():
    print("Welcome to the Shadowrun Combat Manager")
    print("type \"exit\" to close. Type \"help\" for a list of commands for for details on a specific command")
    print()
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
    remove_cmd = cmd.RemoveCombatant(console)
    console.commands["remove"] = remove_cmd
    console.commands["remove-combatant"] = remove_cmd
    console.commands["save"] = cmd.SaveCommand(console)
    console.commands["load"] = cmd.LoadCommand(console)
    console.commands["help"] = cmd.HelpCommand(console)
    console.commands["stun"] = cmd.StunCommand(console)
    console.commands["stun-heal"] = cmd.HealStunCommand(console)
    console.commands["about"] = cmd.AboutCommand()




if __name__ == "__main__":
    start_console()