import typer

app = typer.Typer()


@app.callback()
def callback():
    """
    callback command
    """


@app.command()
def shoot():
    """
    shoot command
    """
    typer.echo("Shoot command called...")


@app.command()
def load():
    """
    load command
    """
    typer.echo("Load command called...")


if __name__ == "__main__":
    app()
