# linstall

A Python CLI to generate a list of installation commands for a package to add to README files.

## Development

- `poetry install`
- `poetry run linstall`

## Notes

- Poetry:
  - [Install/Uninstall Poetry](https://python-poetry.org/docs/master/#installation)
  - `curl -sSL https://install.python-poetry.org | python3 - --preview`
  - `poetry --version`
  - `poetry config --list`
  - `poetry config virtualenvs.in-project true`
  - `poetry add click@latest`
- [Poetry Version Plugin](https://github.com/tiangolo/poetry-version-plugin):
  - `poetry self add poetry-version-plugin`
  - `poetry build`
  - `poetry self remove poetry-version-plugin`
  - [plugin does not work anymore with latest poetry 1.2.0b2](https://github.com/tiangolo/poetry-version-plugin/issues/25) (open) issue.
