# TODO Items

## Framework Integrations

* [ ] [Alembic](https://github.com/sqlalchemy/alembic) is a data migration tool for SQLAlchemy. It is used to generate and run migrations.
* [ ] [Open Telemetry](https://opentelemetry.io/docs/languages/python/) to support server side tracing, etc.
* [ ] [logging](https://docs.python.org/3/library/logging.html) should be configured.
* [ ] [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) to manage settings for the app. This also supports configuaration via `.env` files, `pyproject.toml` and environment variables.

## Code Improvements

* [ ] Use `async` version of `SQLAlchemy` for better performance.
* [ ] Use middleware to validate and inject `User` instance based on phone number in the request.
* [x] Segregate `routes` into `routers` folder and manage them.
* [ ] Convert `Reached` table/model into `Conversations` table/model. This table holds the complete conversation with OpenAI.

## Ref: [FullStack Template](https://github.com/tiangolo/full-stack-fastapi-template)

## Open Question

FrontEnd choice: Simple server side app with bootstrap or ReactJS app?

Example templating:

```jinja
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample Form</title>
</head>
<body>
<form method="post">
    <input type="number" name="num" value="1234"/>
    <input type="submit">
</form>

<p>Result: {{ result }}</p>

</body>
</html>
```

```python
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from src.model import spell_number

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get('/')
def read_form():
    return 'hello world'


@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, num: int = Form(...)):
    result = spell_number(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})
```
