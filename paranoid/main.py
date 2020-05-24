import datetime
import json
import os
import time

import typer
from paranoid.modules import util

app = typer.Typer()


@app.command()
def hide(filename: str, delete: bool = False):
    """Encrypt file

    :param filename: The file to encrypt
    :type filename: str
    :param delete:  Whether to automatically delete the source file, defaults to False
    :type delete: bool, optional
    """
    typer.clear()
    try:
        password: str = typer.prompt("Password", hide_input=True)

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
def show(filename: str):
    """Decrypt file

    :param filename: The file to decrypt
    :type filename: str
    """
    typer.clear()
    try:
        password: str = typer.prompt("Password", hide_input=True)

        content: str = util.read(filename)
        decrypted_content: str = util.decrypt(password, content)
        decrypted_filename: str = f"{os.path.dirname(filename)}/decrypted.dat"

        util.write(decrypted_filename, decrypted_content)

        typer.secho(f"File decrypted as {decrypted_filename}", fg=typer.colors.GREEN)
        typer.secho(f"Content: \n{decrypted_content}", fg=typer.colors.GREEN)
    except Exception as ex:
        typer.secho(f"Error: {ex}", fg=typer.colors.RED)


@app.command()  # noqa: C901
def token(filename: str):
    """Generate OTP

    :param filename: Ecrypted file to read authenticator keys
    :type filename: str
    """
    typer.clear()
    try:
        password: str = typer.prompt("Password", hide_input=True)

        content: str = util.read(filename)
        decrypted_content: str = util.decrypt(password, content)

        data: dict = json.loads(decrypted_content)
        options: dict = {
            str(list(data.keys()).index(k) + 1): k for k, v in data.items()
        }
        options["0"] = "EXIT"

        typer.echo(f"\nSelect an account:")
        for k, v in options.items():
            typer.echo(f"    {k} - {v}")
        choice: str = None

        while choice not in options.keys():
            choice = typer.prompt("    Selected")

        if choice == "0":
            typer.echo("Aborted!")
        else:
            account_key: str = options[choice]
            typer.echo(f"\n OTP for {account_key}:")

            seconds: int = datetime.datetime.now().second
            elapsed: int = seconds if seconds < 30 else seconds - 30

            for i in range(3):
                if i > 0:
                    typer.echo(f"\033[2A")

                code: str = util.get_otp(account_key)
                label: str = f"    \033[32m{code}\033[0m"
                with typer.progressbar(
                    length=30, label=label, show_percent=False, show_eta=False
                ) as progress:
                    if elapsed > 0:
                        progress.update(elapsed)
                    for second in range(30 - elapsed):
                        time.sleep(1)
                        progress.update(1)
                        typer.echo(f" Remaining: {30-elapsed-second-1:0>2}s", nl=False)
                    if elapsed > 0:
                        elapsed = 0
    except Exception as ex:
        typer.secho(f"Error: {ex}", fg=typer.colors.RED)


if __name__ == "__main__":
    app()
