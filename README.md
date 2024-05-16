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

# Linting with ruff
ruff check --fix
```

## To run in cmdline

```bash
fastapi dev src/main/app.py
```

## Postgres Pod

Podman is used to create the local postgres database. To create a pod, run the following command:

```bash
podman kube play docker/deployment.yaml
```

To Stop the pod:
```bash
podman pod stop textblast
```

To start the pod:
```bash
podman pod start textblast
````

## Alembic

Initialize Alembic

```bash
alembic init --template generic ./alembic
```

Edit .ini to setup the connection to the database.

```ini
[alembic]
sqlalchemy.url = postgresql://postgres:postgres@localhost:5432/postgres
timezone = UTC
```

Create a migration script

```bash
alembic revision -m "Create user table"
```

Run the first migration

```bash
alembic upgrade head
```
