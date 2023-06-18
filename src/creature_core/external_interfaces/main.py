import typer

from creature_core.external_interfaces.apps.auto_farm import auto_farm_app

app = typer.Typer()

app.add_typer(auto_farm_app, name="auto-farm")


@app.command()
def good(name: str):
    print(name)


if __name__ == "__main__":
    app()
