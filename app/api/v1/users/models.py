from app.api.v1.utils.validators import Validators
from app import create_app, bcrypt
from flask import jsonify

users_list = [
	{
		'id': 0,
		'username': 'Charles',
		'password': 'password',
		'email': 'charles@demo.com',
		'timestamp': '2018, 12, 17, 8, 24, 43, 312403'
		},
	{
		'id': 1,
		'username': 'Elvis',
		'password': 'password',
		'email': 'Elvis@demo.com',
		'timestamp': '2018, 12, 17, 8, 24, 43, 312403'
		},
	{
		'id': 2,
		'username': 'Susan',
		'password': 'password',
		'email': 'Susan@demo.com',
		'timestamp': '2018, 12, 17, 8, 24, 43, 312403'
	}
]

validate = Validators()

class Users():

	def signup(self, email, username, password, timestamp):
				
		if validate.is_valid_password(password) is False:
			return {"message": "password does not meet requirements"}
		if validate.is_valid_username(username) is False:
			return {"message": "Username must be a string of at least 3 characters"}
		if validate.is_valid_email(email) is False:
			return {"message": "Provide valid email of the correct format"}
		else:
			id = len(users_list) + 1
			# username = data('username')
			# password = data.get('password')
			# email = data.get('email')
			# timestamp = datetime.datetime.now()
			hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
			new_user = {'id': id, 'username': username, 'password': hashed_password, 
						'email': email, 'timestamp': timestamp}
			users_list.append(new_user)
			return {
				"message": "New user added with the following details",
				"User created": username,
				"Encrypted password": hashed_password,
				"time created": timestamp
				}


	def get_all(self):
		if len(users_list) == 0:
			return {"message": "Empty list"}
		else:
			return users_list

	def delete_user_by_id(self, user_id):
		for user in users_list:
			if user['id'] == user_id:
				users_list.remove(user)
				return {"message": "User with id {} has been deleted!!!".format(user_id)}
				# return user
			else:
				return {"message": "No user found with that id"}
	
	def find_user_by_id(self, user_id):
		for user in users_list:
			if user['id'] == user_id:
				return user
			else:
				return {"message": "No user found with that id"}
	''' This API is for updating user details, not complete yet  '''
	def update_user_parameters(self, user_id):
		for user in users_list:
			if user['id'] == user_id:
				return {"The user details have been updated successfully", user}
			else:
				return  {"message": "User not found, no changes made"}
	def login_user(self, username, password):
		for user in users_list:
			if user['username'] == username and user['password'] == password:
				return {"message": "user {}, logged in successfully".format(username)}
			else:
				return {"message": "check your username or password"}