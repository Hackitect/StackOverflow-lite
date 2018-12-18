from flask import Blueprint, request, jsonify, json, abort
import datetime
from app.api.v1.users import models
# from api.auth.utils import Validate
# later we shall need to put all the functions in this route in main utils model


auth = Blueprint('auth', __name__)

user_object = models.Users()


# api to return all users in the system
@auth.route("/api/v1/auth/all", methods=['GET'])
def user_all():
	return jsonify(user_object.get_all())

# find user by ID
@auth.route("/api/v1/auth/<int:user_id>", methods=['GET'])
def user_id(user_id):
	return jsonify(user_object.find_user_by_id(user_id))

# api to delete user from system
@auth.route("/api/v1/auth/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):	
	return jsonify(user_object.delete_user_by_id(user_id))


# api to signup user in the system
@auth.route("/api/v1/auth/signup", methods=['POST'])
def signup_user():
	if not request.json or not 'username' in request.json or not 'email' in request.json or not 'password' in request.json:
		return jsonify ({"label":"username, email and password fields required"}), 400
	
	else:
		
		username = request.json['username']
		password = request.json['password']
		email = request.json['email']
		timestamp = datetime.datetime.now()

		# id = len(models.users_list) + 1
		# new_user = {'id': id, 'username': username, 'password': password, 'email': email, "timestamp": timestamp}
		# models.users_list.append(new_user)

		# return jsonify(new_user)

		return jsonify(user_object.signup(email, username, password, timestamp)), 201

		
	

# api to update userdetails with particular id
@auth.route("/api/v1/auth/update", methods=['PUT'])
def update_user():	

	#Check that the request string JSON format, and ID is required
	if not request.json or not 'id' in request.json:
		abort(404)
	else:		
		id = request.json['id']
		username = request.json['username']
		password = request.json['password']
		email = request.json['email']
		return jsonify(user_object.update_user_parameters())

# api to login user
@auth.route("/api/v1/auth/login", methods=['POST'])
def login_user():	

	#Check that the request string is in JSON format, ID is required
	if not request.json or not 'username' in request.json or not 'password' in request.json:
		abort(400)
	else:
		username = request.json['username']
		password = request.json['password']
		# email = request.json['email']
		return jsonify(user_object.login_user(username, password)), 200			
