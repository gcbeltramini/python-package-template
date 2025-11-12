# python-package-template

A minimal Python package template.

## Development

### Installation

```bash
uv venv --python=3.13
source .venv/bin/activate
uv pip install -e .
```

### Running tests

```bash
uv pip install -e '.[test]'
uv run coverage run -m pytest # run unit tests with 'pytest', and measure code execution
uv run coverage report --fail-under=95 # report coverage statistics, and exit with a status of 2 if the total coverage is less than the threshold
```

## Usage

```python
import my_package
```
