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