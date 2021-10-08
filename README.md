# README #

Monorepo for handling python projects

## Install of precommit
You can run
```sh
pre-commit install
rm -rf ~/.cache/pre-commit
pip install -r requirements-dev.txt
```
to install [pre-commit](https://pre-commit.com) hooks

## Install of Poetry
Install [poetry](https://python-poetry.org/docs/)
```sh
    cd integration
    poetry init
    poetry update
    poetry add <modules>
```
Problems can occure that ipython don't reconize venv

## Install of pyenv
Use brew on mac, install 3.9+ using pyenv. Each container will have its each pyproject.toml and its dependices.
Reason for this that each container will use poetry to install pyhon packages.

Top level pyproject.toml is create accordinly and made for coding standards

```sh
    export PATH="$HOME/.poetry/bin:$PATH"
    pyenv virtualenv 3.9.7 python-project
    cd python-project
    pyenv local python-project
    poetry init
    poetry add -D black flake8 <other dev>
    ## used when poetry and pyenv dont work
    poetry env use python
```


## Properties for asset
If **replace_columns** exists in assest than it has prescenden over other formatting rules. That means that custom operation should be based on after replace_column has done its replacment.
