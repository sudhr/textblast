# TODO Items

## Framework Integrations

* [x] [Alembic](https://github.com/sqlalchemy/alembic) is a data migration tool for SQLAlchemy. It is used to generate and run migrations.
* [ ] [Open Telemetry](https://opentelemetry.io/docs/languages/python/) to support server side tracing, etc.
* [ ] [logging](https://docs.python.org/3/library/logging.html) should be configured.
* [ ] [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) to manage settings for the app. This also supports configuaration via `.env` files, `pyproject.toml` and environment variables.
* [ ] [python-lambda-local](https://pypi.org/project/python-lambda-local/) to setup the app to run as AWS λ function. This [guide](https://www.deadbear.io/simple-serverless-fastapi-with-aws-lambda/) helps setting up FastAPI as AWS λ function.
* [x] Use Postgres DB with [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) and Alembic. Set this up in a podman pod.

## Code Improvements

* [ ] Use middleware to validate and inject `User` instance based on phone number in the request.
* [x] Segregate `routes` into `routers` folder and manage them.
* [ ] Convert `Reached` table/model into `Conversations` table/model. This table holds the complete conversation with OpenAI.
* [ ] Use [Pydantic Logfire](https://pydantic.dev/logfire) for logging and tracing.
* [ ] Use [Pydantic Validators](https://docs.pydantic.dev/latest/concepts/validators/) to validate input values.
* [x] Use custom Postgres schema. See [here](https://stackoverflow.com/questions/73068830/alembic-postgres-how-to-switch-to-another-schema) for more details.
