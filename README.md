# **TRIVIA API - Documentation and API Reference**

## Trivia App Introduction

The Trivia app is an interface that Udacity uses to enable creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app, and play a quiz game!.

## Authors
Jany Muong


## Acknowledgements
I'd love to acknowledge the contribution of many people within the Udacity fullstack programme space, but for the limitation of documentation space.
This work is a success because of the immense resources from the Udacity classroom, thanks to Udacity.


## Basic Functionality - Trivia App

The app is built around `CRUD` operations uing python and related libraries and of course the frontend. The scope of its functionality includes:

1. Displays questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.


## Getting Started and Local development

[Fork](https://help.github.com/en/articles/fork-a-repo) the project repository and [clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository.


### Tech Stack

Developers should have `node, python3, pip` and other relevant backend and frontend stack as listed out in the preview below that points to _Backend README_ and _Frontend REAME_ documentations:


### Backend

The [backend](./backend/README.md) directory contains the requisite Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

> View the [Backend README](./backend/README.md) for craeting siloed python virtual environments and `TODOS` tasks.


### Tests
Deploying Tests in your Local Enivronment. Prior to running the tests, set up and populate the testing database:
Run the following commands in `backend` directory that hosts `trivia.psql`

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
```

Use `psql -U username trivia_test < trivia.psql` in ***Windows***


To deploy the tests, and with activated virtual environment run the following command in terminal:

`python test_flaskr.py`


### Frontend

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

#### Frontend expectations
1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads?

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. `frontend/src/components/QuestionView.js`
2. `frontend/src/components/FormView.js`
3. `frontend/src/components/QuizView.js`

> View the [Frontend README](./frontend/README.md) for more detailed instructions setting up the frontend server.



## **API reference**

### Base URL
Currently the trivia app runs on localhost:
Open [http://localhost:3000](http://localhost:3000) to access Trivia API.



### Errors 

Errors are returned in json format:
```json
{
    "success": False, 
    "error": 422,
    "message": "request unprocessable"
}
```
Trivia app returns the following error codes: 400, 404, 405, 422, 500 and with these corresponding messages:
- 400 - 'bad request'
- 404 - 'resource not found'
- 405 - 'method not allowed'
- 422 - 'request unprocessable'
- 500 - 'internal server error'



### Resources and Endpoints

`GET /categories`
`curl -X GET http://127.0.0.1:5000/categories`

* General
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None

* Response
* status: 200
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs.

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```

---

`GET /questions`
`curl -X GET http://127.0.0.1:5000/questions?page=1`
* General:
- Fetches a paginated set of questions, a total number of questions, all categories and current category string.
- Request Arguments: `page` - integer
* Response:
* status: 200
- Returns: An object with 10 questions a page, total questions-int, object including all categories, and current category for each question-string.

```json
 {"categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 20
}

```

---

`POST /questions`
`curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"question":"When was REACT first released", "answer":"look up in Google", "difficulty":"1", "category":"1"}'`
* General
* Request body
- sends a create question operation to the backend 
- Request args: `question`, `answer` - string, `difficulty` - integer
* Response:
- Status: 200
- Returns: An object with question `id`- integer, `success` - boolean

```json
{
  "created": 24,
  "success": true
}

```
---

`GET /categories/${id}/questions`
`curl -X GET http://127.0.0.1:5000/categories/1/questions`

* General:
- Fetches questions for a cateogry specified by id request argument
- Request Arguments: category `id` - integer

* Response: http status code 200
- Returns: An object with questions for the specified category, total questions, and current category for the questions

```json
{
  "current_category": "Science",
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "look up in Google",
      "category": 1,
      "difficulty": 1,
      "id": 24,
      "question": "When was REACT first released"
    }
  ],
  "success": true,
  "total_questions": 4
}
```

---

`DELETE '/questions/${id}'`
`curl -X DELETE http://127.0.0.1:5000/questions/27`
* General:
- Deletes a specified question using the id of the question
* Request Arguments: `id` - integer
* Response: http - status 200
- Returns: Does not need to return anything besides the appropriate HTTP status code. Optionally can return the id of the question. If you are able to modify the frontend, you can have it remove the question using the id instead of refetching the questions.
```json
{
  "deleted": 27,
  "success": true
}
```


---

`POST '/quizzes'`
`curl -X POST http://127.0.0.1:5000/quizzes -H "Content-Type: application/json" -d '{"quiz_category": {"id":"1"}, "previous_questions": []}'`
* General:
- Sends a post request in order to get the next question
- Request Body: args - quiz_category-`id` integer, or string, `previous_questions`- list:

```json
{
    "quiz_category": {"id":"1"}, "previous_questions": []
 }
```
* Response: status OK
- Returns: a single new question object

```json
{
  "question": {
    "answer": "Blood",
    "category": 1,
    "difficulty": 4,
    "id": 22,
    "question": "Hematology is a branch of medicine involving the study of what?"
  },
  "success": true
}
```

---

`POST '/questions/search'`
`curl -X POST http://127.0.0.1:5000/questions/search -H "Content-Type: application/json" -d '{"searchTerm": "title"}'`
* General:
- Sends a post request in order to search for a specific question by search term: `searchTerm` - string
- Request Body:

```json
{
  "searchTerm": "title"
}
```
* Response: status 200
- Returns: any array of questions, a number of total_questions that met the search term and the current category string

```json
{
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ],
  "success": true,
  "total_questions": 2
}
``` 
