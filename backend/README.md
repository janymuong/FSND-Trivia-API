# **TRIVIA API**

## Trivia API Backend
 This is a **fullstack** web app backend. Read through the backend documentation to install its dependencies.

# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** and **PIP**- Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - It's recommended to leverage a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

If you have pip virtualenv already installed; create a siloed python environment. Run in your backend directory:

```bash
python -m virtualenv venv
```

To activate virtual venv on ***Windows*** run:

```bash
venv\Scripts\activate
```

The equivalent command on ***UNIX-based operating systems*** run:

```bash
source venv/bin/activate
```

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `__init__.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

The analogous command for Windows environment:

```bash
create database trivia;
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

The equivalent dump in Windows is:

```bash
psql -U username trivia < trivia.psql
```

### Run the Server

From within the root backend directory and with activated virtual environment...

To run the server, execute:

```bash
set FLASK_APP=flaskr
```
```bash
set FLASK_ENV=development
```
```bash
flask run
```

The analogous commands for UNIX based systems are:

```bash
export FLASK_APP=flaskr
```
```bash
export FLASK_ENV=development
```
```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `GET` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting API Endpoints

Provided detailed documentation and reference of the API endpoints including the URL, request parameters, and the response body are in the API documentation reference README markdown file in the root directory of the TRIVIA API app.

> View [Trivia API Documentation and API Reference](../README.md) for sample requests and responses and endpoints behavior.