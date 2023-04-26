import os
from unicodedata import category
from flask import Flask, request, abort, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

# pagination function for 10 questions a page,
# and will be called on relevant endpoints:
def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    
    with app.app_context():
        setup_db(app)


    """
    @TODO: Set up CORS. Allow '*' for origins.
    Delete the sample route after completing the TODOs
    """
    # enable cors and allow for origins
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    CORS(app)
    
    
    """
    @TODO: Use the after_request decorator to set Access-Control-Allow 
    """
    # after_request decorator
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type,Authorization,true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET,POST,DELETE,PATCH,PUT'
        )
        return response
    
    
    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories')
    def retrieve_categories():
        '''
        GET request to retrieve all categories
        '''
        query = Category.query.order_by(Category.id).all()
    
        if len(query) == 0:
            abort(405)
            
        else:
            # category.id: category.type for category in query:
            # format expected by frontend, FE.
            categories = { category.id: category.type for category in query }
            return jsonify(
                {
                    'success': True,
                    'categories': categories,
                    'total_categories': len(Category.query.all())
                }
            )

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/questions')
    def retrieve_questions():
        '''
        GET request to retrieve questions, paginated: using prior defined f(n) paginate_questions()
        '''
        # total questions, current category for each question, categories.
        categories = Category.query.order_by(Category.id).all()
        
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)
        
        if len(current_questions) == 0:
            abort(404)
        # category.id: category.type for category in categories
        # returns the expected format to FE
        return jsonify(
            {
                'success': True,
                'questions': current_questions,
                'total_questions': len(selection),
                'categories': {
                    category.id: category.type for category in categories
                    }
            }
        )


    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route('/questions/<int:id>', methods=['DELETE'])
    def delete_question(id):
        '''
        Endpoint for: DELETE a question
        '''
        # select question by Question.id to be passed into the delete() function
        question = Question.query.filter(Question.id == id).one_or_none()
        
        if question is None:
            abort(422)
            
        if question:
            question.delete()

            return jsonify(
                {
                    'success': True,
                    'deleted': id
                }
            )

        else:
            abort(404)
            

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    # TIP: a person can look up a question
    # to check(using search on /questions/search endpoint)
    # IF EXISTS before adding it.
    @app.route('/questions', methods=['POST'])
    def create_question():
        '''
        POST endpoint to add a new question. 
        '''
        body = request.get_json()
        # create question with values for each field from the request body
        try:
            question = Question(question=body.get('question'),
                            answer=body.get('answer'),
                            difficulty=body.get('difficulty'),
                            category=body.get('category')
                )
            
            question.insert()

            return jsonify(
                {
                    'success': True,
                    'created': question.id
                }
            )

        except:
            abort(405)


    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        '''
        POST to look up questions based a 'search' term
        '''
        body = request.get_json()
        searchTerm = body.get('searchTerm', None)
        if searchTerm:
            # search term formatted()
            selection = Question.query.order_by(Question.id).filter(
                Question.question.ilike(f'%{searchTerm}%')
            )
            questions = paginate_questions(request, selection)

            return jsonify(
                {
                    'success': True,
                    'questions': questions,
                    'total_questions': len(selection.all())
                }
            )
        if selection is None:
            abort(404)

    
    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/categories/<int:id>/questions', methods=['GET'])
    def categorised_questions(id):
        '''
        GET endpoint for questions based on category
        '''
        # select Category that you want 
        # (and using Question.category attribute )
        # .get all the questions under it paginated
        # category name is returned in json-
        # with category.type, from Category's 'type' attribute
        
        category = Category.query.filter(Category.id == id).one_or_none()
        if category:
            selection = Question.query.filter(Question.category == id).order_by(Question.id)
            questions = paginate_questions(request, selection)

            # 'current_category': category.type returns expected category name-string
            return jsonify(
                {
                    'success': True,
                    'questions': questions,
                    'total_questions': len(selection.all()),
                    'current_category': category.type
                    
                }
            )
        else:
            abort(422)
    
    

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    # 'Trivia' endpoint 
    @app.route('/quizzes', methods=['POST'])
    def quiz_game():
        ''' 
        Play quiz game: randomize questions 
        '''
        try:
            body = request.get_json()
            previous_questions = body.get('previous_questions', None)
            quiz_category = body.get('quiz_category', None)
             
            if quiz_category:
                # query quiz list of questions 
                # based on user's quiz_category(Question.category == quiz_category['id])
                quiz_list = Question.query.filter(Question.category == quiz_category['id']).all()
                
                if quiz_category['id'] == 0:
                    # all randomized questions quiz list for clicking 'ALL' category
                    quiz_list = Question.query.order_by(Question.id).all()
        
            # list of available IDs in quiz_list
            # then generate randmo_num out of IDs using list method random.choice
            available_ids = [question.id for question in quiz_list]
            random_num = random.choice([num for num in available_ids if num not in previous_questions])
            
            # random question using random_num(as id) that match Question.id field
            question = Question.query.filter(Question.id == random_num).one_or_none()
            previous_questions.append(question.id)
            print('count previous_quetions', len(previous_questions))
            
            return jsonify(
                {
                    'success': True,
                    'question': question.format()
                }
            )
            
        except:
            abort(404)       
    


    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    # error handlers for expected app behavior
    @app.errorhandler(400)
    def bad_request(error):
        return (jsonify({'success': False,
                        'error': 400,
                        'message': 'bad request'}),
        400
        )

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({'success': False,
                     'error': 404,
                     'message': 'resource not found'}),
            404
        )

    @app.errorhandler(405)
    def not_allowed(error):
        return (
            jsonify({'success': False,
                     'error': 405,
                     'message': 'method not allowed'}),
            405
        )
        
    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({'success': False,
                     'error': 422,
                     'message': 'request unprocessable'}),
            422
        )

    @app.errorhandler(500)
    def server_error(error):
        return (
            jsonify({'success': False,
                     'error': 405,
                     'message': 'Internal Server error'}),
            500
        )
    return app