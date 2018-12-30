from flask import Blueprint, jsonify, request
from app.api.v1.questions import models
import datetime

questions = Blueprint('questions', __name__, url_prefix='/api/v1')


qu_object = models.Questions()


@questions.route("/questions", methods=['GET'])
def get_question():
	return jsonify(qu_object.get_all())

@questions.route("/questions", methods=['POST'])
def post_question():

	# we are expecting our json request in this example format 
	# {"user_id": 2, "question": "what is the Value of Pi"}
	if not request.json or not 'question' in request.json or not 'user_id' in request.json:
		return jsonify ({"label":"you must be logged in to post a questions"}), 400
	
	else:
		
		user_id = request.json['user_id']
		question = request.json['question']
		timestamp = datetime.datetime.now()

		return jsonify(qu_object.post_question(user_id, question, timestamp))


@questions.route("/questions/<int:questionId>", methods=['DELETE'])
def del_question(questionId):
	# if not request.json or not 'questionId' in request.json:
	# 	return jsonify ({"label":"you must be logged on and enter questionId"})
	return jsonify(qu_object.delete_question(questionId))

@questions.route("/questions/<int:questionId>", methods=['GET'])
def fetch_question(questionId):
	return jsonify(qu_object.fetch_specific_question(questionId))

@questions.route("/questions/<questionId>/answers", methods=['POST'])
def post_answer(questionId):
	data = request.get_json
	userId = data['userId']
	answer = data['answer']
	return jsonify(qu_object.post_answer(questionId, userId, answer))

