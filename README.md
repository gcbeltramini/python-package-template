# python-package-template

A minimal Python package template.

## Usage

Install the project and its dependencies: `uv sync --frozen --all-extras --dev`

This will create or update the Python venv folder `.venv`, using the Python version from file
`.python-version`, and the dependencies from file `uv.lock`.

### Terminal

Activate the `venv` and run the Python commands. Example:

```shell
source .venv/bin/activate
python3 -c "from my_package import my_functions; print(my_functions.foo(2))"
```

If you update the code, you don't need to do anything (e.g., it's not necessary to reinstall the
library, or update the `venv`).

### Jupyter notebook

Install `jupyter` in an isolated environment and run `jupyter lab`:

```shell
uv run --with jupyter jupyter lab
```

In a Jupyter notebook with the Python 3 kernel `ipykernel`, run the Python commands. Example:

```python
from my_package import my_functions
print(my_functions.foo(2))
```

If you update the code, restart the Jupyter kernel in the Jupyter notebook to use the new version.

## Development

- Install the project and its dependencies: `uv sync --locked --all-extras --dev --verbose`

  - This will create or update the Python `venv` folder `.venv`.
  - The parameter `--locked` asserts that the `uv.lock` will remain unchanged and is up-to-date.
    If it's not, the following error will occur:

    ```text
    The lockfile at `uv.lock` needs to be updated, but `--locked` was provided. To update the lockfile, run `uv lock`.
    ```

    In that case, run `uv lock` to update the lockfile.

    Using `--locked` is equivalent to running `uv lock --check` before syncing, because this
    command checks if the `uv` lockfile `uv.lock` is up-to-date. The error message is similar.

- Run `ruff` for linting: `uv run ruff check .`
- Run unit tests with `pytest` and measure code coverage with `coverage.py`: `uv run coverage run -m pytest`
- Test code coverage with `coverage.py`: `uv run coverage report`
  - The threshold is defined in file `pyproject.toml`, under `[tool.coverage.report]` --> `fail_under`
- Update the `uv` lockfile: `uv lock`
