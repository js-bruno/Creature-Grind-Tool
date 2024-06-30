import typer
from simple_term_menu import TerminalMenu

from creature_core.controller import AutoFarmController

if __name__ == "__main__":
    options = ["auto-farm", "ev-up", "shine-hunt"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        typer.echo("RUNNING AUTOFARMING!...")
        AutoFarmController.auto_farm_start()
