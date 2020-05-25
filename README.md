### Starting from scratch
```
# install poetry
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# create new project
$ poetry new typer-basic-skeleton
$ cd typer-basic-skeleton

# initialize as a git repo
$ git init .

# update pyproject.toml set python to ^3.6
# add typer dependency
$ poetry add typer[all]
```

### Manual test
```
# Encrypt a file
$ make run ARGS="hide ./tests/data/account.json ~/.paranoid/encrypted.dat"

# Show file's decrypted content on console
$ make run ARGS="show ~/.paranoid/encrypted.dat"

# Export file's decrypted content to a file
$ make run ARGS="show ~/.paranoid/encrypted.dat --export=~/Desktop/exposed.json"

# Get OTP from a specific file
$ make run ARGS="token ~/.paranoid/encrypted.dat"

# Get OTP from default location
$ make run ARGS="token"
```