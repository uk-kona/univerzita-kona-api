# univerzita-kona-api

## Development

This project uses [poetry](https://python-poetry.org/) to manage its dependencies.
You can get it from [here](https://github.com/python-poetry/poetry#installation).

```sh
# clone repo
git clone git@github.com:uk-kona/univerzita-kona-api.git

# install dependencies
poetry install

# spawn shell within virtual environment
poetry shell

export FLASK_APP=app
export FLASK_ENV=development

# run dev server
flask run

# create database
flask db init

# create migrations
flask db migrate

# apply migrations
flask db upgrate
```
