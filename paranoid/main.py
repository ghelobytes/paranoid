import os

import typer
from paranoid.modules import util

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


@app.command()
def hide(
    filename: str, password: str = typer.Option(..., prompt=True), delete: bool = False
):
    """Encrypt file

    :param filename: The file to encrypt
    :type filename: str
    :param delete:  Whether to automatically delete the source file, defaults to False
    :type delete: bool, optional
    """
    try:
        content: str = util.read(filename)
        encrypted_content: str = util.encrypt(password, content)
        encrypted_filename: str = f"{os.path.dirname(filename)}/encrypted.dat"

        util.write(encrypted_filename, encrypted_content)
        if delete:
            os.remove(filename)

        typer.secho(f"File encryped as {encrypted_filename}", fg=typer.colors.GREEN)
        typer.secho(f"Content: \n{encrypted_content}", fg=typer.colors.GREEN)
    except Exception as ex:
        typer.secho(f"Error: {ex}", fg=typer.colors.RED)


@app.command()
def show(filename: str, password: str = typer.Option(..., prompt=True)):
    try:
        content: str = util.read(filename)
        decrypted_content: str = util.decrypt(password, content)
        decrypted_filename: str = f"{os.path.dirname(filename)}/decrypted.dat"

        util.write(decrypted_filename, decrypted_content)

        typer.secho(f"File decrypted as {decrypted_filename}", fg=typer.colors.GREEN)
        typer.secho(f"Content: \n{decrypted_content}", fg=typer.colors.GREEN)
    except Exception as ex:
        typer.secho(f"Error: {ex}", fg=typer.colors.RED)


if __name__ == "__main__":
    app()
