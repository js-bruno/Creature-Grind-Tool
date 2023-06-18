import typer

from creature_core.controller import AutoFarmController

auto_farm_app = typer.Typer()


@auto_farm_app.command()
def run():
    typer.echo("RUNNING AUTOFARMING!...")
    AutoFarmController.auto_farm_start()
