# linstall

A Python CLI to generate a list of installation commands for a package to add to README files.

## Development

- `poetry install`
- `poetry run linstall`
- `poetry check`

## Notes

- Poetry:
  - [Install/Uninstall Poetry](https://python-poetry.org/docs/master/#installation)
  - `curl -sSL https://install.python-poetry.org | python3 - --preview`
  - `poetry --version`
  - `poetry config --list`
  - `poetry config virtualenvs.in-project true`
  - Dependencies:
    - Add the dependencies and just leave the version number in the `pyproject.toml` file for exact versions
    - `poetry add click markdown-subtemplate pyperclip`
    - `poetry add black isort --group dev`
  - Delete the virtual environment: `poetry env remove python` ([source](https://github.com/python-poetry/poetry/issues/926#issuecomment-710056079))
- [Poetry Version Plugin](https://github.com/tiangolo/poetry-version-plugin):
  - `poetry self add poetry-version-plugin`
  - `poetry build`
  - `poetry self remove poetry-version-plugin`
  - [plugin does not work anymore with latest poetry 1.2.0b2](https://github.com/tiangolo/poetry-version-plugin/issues/25) (open) issue.
