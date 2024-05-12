# Text Blaster

## Build Instructions

```bash
pip install '.[test,dev]'

# To run tests with coverage
coverage run --branch -m pytest

# Generate HTML coverage report
coverage html

# Open in the default browser in linux
xdg-open htmlcov/index.hml
```

## To run in cmdline
```bash
fastapi dev src/webbook/app.py
```
