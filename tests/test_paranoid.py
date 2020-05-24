from paranoid.main import app
from typer.testing import CliRunner

runner = CliRunner()


INPUT: str = "s0m3secrets"


def test_hide():
    result = runner.invoke(app, ["hide", "./tests/data/account.json"], input=INPUT)
    print("\nresult.stdout:\n", result.stdout)
    assert result.exit_code == 0


def test_show():
    result = runner.invoke(app, ["show", "./tests/data/encrypted.dat"], input=INPUT)
    print("\nresult.stdout:\n", result.stdout)
    assert result.exit_code == 0


def test_token():
    result = runner.invoke(
        app, ["token", "./tests/data/encrypted.dat"], input=f"{INPUT}\n0"
    )
    print("\nresult.stdout:\n", result.stdout)
    assert result.exit_code == 0
    assert "Aborted" in result.stdout
