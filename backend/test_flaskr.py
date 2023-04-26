import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
from dotenv import load_dotenv

# load .env file in backend dir using python-dotenv lib
path = os.path.dirname(os.path.dirname(__file__))
env_file = os.path.join(path, ".env")
load_dotenv(env_file)

'''
# TIP or DISCLAIMER(I don't know what to call this):
# I was unable to do tests using environment variables in conn uri, both in models.py and test_flaskr.py ##testing_only
# for tests to work, make sure you use plain credentials in both models.py and test_flaskr.so you might want to
# use the connection syntax that is commented out(instead of the active self.database_path).
# at least this is what worked for me. and I couldn't figure out where the error came from if I used environment variables in testing.
# if I did otherwise i.e using environment variables there was an error about Host name is 'none' 
# (only when running: python test_flaskr.py) in terminal: See bottom of this file for more info:
# TRUE:environment varaibles work fine when I'm running flaskr.

# for models.py when testing you might want to use this: [should be credentials in plain text in both files for testing]
# database_path = "postgresql://{}:{}@{}/{}".format("postgres", "yourpass", "localhost:5432","trivia")
# for test_flaskr.py:
# self.database_path = "postgresql://{}:{}@{}/{}".format("postgres", "yourpassword", "localhost:5432","trivia_test")
'''

# normal flow of code here;
# read variables from .env file with os.getenv() to connect to trivia_test db
class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = os.getenv('DB_TEST')
        self.db_host = os.getenv('DB_HOST')
        self.db_password = os.getenv('DB_PASS')
        self.db_user = os.getenv('DB_USER')
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(self.db_user, self.db_password, self.db_host, self.database_name)
        setup_db(self.app, self.database_path)
        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
        # test data for creationg a new question
        self.test_question = {
            'question': "what language was used to write the first C lang",
            'answer': "Look up in google search",
            'difficulty': 1,
            'category': 1
            }
        
        # test data for generating a random question
        self.random_question = {"quiz_category": {"id": 1},
                             "previous_questions": []
                             }
    def tearDown(self):
        '''Executed after each endpoint test'''
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    ## TESTS for retrieve categories_GET
    def test_200_retrieve_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_categories'])
        self.assertTrue(len(data['categories']))
        
    def test_405_invalid_retrive_catgories(self):
        res = self.client().get('/categories/7', json={'foo': 1})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
    
    
    ## TESTS for paginated questions_GET
    def test_200_retrieve_paginated_questions(self):
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        
    def test_404_retrieve_beyond_valid_questions_page(self):
        res = self.client().get('questions/?page=73', json={'pagefoo': 73})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        
        
    ## TESTS DELETE endpoint questions_DELETE
    def test_200_delete_question(self):
        res = self.client().delete('/questions/17')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 17).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 17)
    
    def test_422_failed_delete_question(self):
        res = self.client().delete('/questions/79')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'request unprocessable')
        

    ## TESTS create question_POST
    def test_200_add_question(self):
        res = self.client().post('/questions', json=self.test_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['created'], 24)

    def test_422_failed_add_question(self):
        res = self.client().post('/questions/7', json=self.test_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertFalse(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')
        self.assertEqual(data['error'], 405)
        
        
    ### TESTS questions/seach questions_POST
    def test_200_search_questions_results(self):
        res = self.client().post('/questions/search', json={"searchTerm": "title"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']), 2)
        self.assertEqual(data['total_questions'], 2)

    def test_200_no_search_results(self):
        res = self.client().post('/questions/search', json={"searchTerm": "GTA"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'], 0)
        self.assertEqual(len(data['questions']), 0)
    
    def test_404_invalid_search(self):
        res = self.client().post('/questions/search/1', json={"searchTerm": "GTA"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['error'], 404)


    ## TESTS for ENDPOINT:questions based on categories_GET
    def test_200_categorised_questions(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['current_category'])
        self.assertTrue(len(data['questions']))
        
    def test_404_invalid_catgorised_questions(self):
        res = self.client().get('/categories/1/questions/7', json={'foo': 1})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')
        

    ## TESTS for quizzes_POST
    def test_200_quizz(self):
        '''
        Quiz test for Caegorised randomized questions
        '''
        res = self.client().post('/quizzes', json=self.random_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

    def test_200_quiz_all(self):
        '''
        Test for all not categorised random question
        '''
        res = self.client().post('/quizzes', json={"quiz_category": 0,"previous_questions": []})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_404_failed_quizz(self):
        '''
        Test for out_of_range_category random question
        '''
        res = self.client().post('/quizzes', json={"quiz_category": 73,"previous_questions": []})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')
                         
                         
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

# ERROR: only when running tests using environment variables from a .env file
# error I was unable to trace where it came from even with correct log in credentials. I asked three times on slack, but no successfully. 
# I tried all means I know, for good measure. I couldn't tell what the problem was, even with stackoverflow

# part of the error(last lines of tracebook):
# conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
# sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not translate host name "None" to address: Unknown host

# (Background on this error at: https://sqlalche.me/e/14/e3q8)