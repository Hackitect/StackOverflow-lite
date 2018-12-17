
# import request
from api.auth.utils import validate_password, validate_username, validate_email

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

class Users():

	def signup(self, email, username, password, timestamp):
				
		if validate_password(password) is False:
			return {"Password does not meet requirements"}
		if validate_username(username) is False:
			return {"Username must be a string of at least 3 characters"}
		if validate_email(email) is False:
			return {"Provide valid email format"}
		else: 
			id = len(users_list) + 1
			new_user = {'id': id, 'username': username, 'password': password, 'email': email, 'timestamp': timestamp}
			users_list.append(new_user)
			return {"New user added with the following details"}

	def get_all(self):
		if len(users_list) == 0:
			return {"message": "Empty list"}
		else:
			return users_list

	def delete_user_by_id(self, user_id):
		for user in users_list:
			if user['id'] == user_id:
				users_list.remove(user)
				return {"message": "User has been deleted!!!"}
				return user
			else:
				return {"message": "No user found with that id"}
	
	def find_user_by_id(self, user_id):
		for user in users_list:
			if user['id'] == user_id:
				return user
			else:
				return {"message": "No user found with that id"}
	
	def update_user_parameters(self, user_id):
		for user in users_list:
			if user['id'] == user_id:
				user = {'id': id, 'username': username, 'password': password, 'email': email}
				return {"The user details have been updated successfully", user}, 200
			else:
				return  {"message": "User not found, no changes made"}, 404
	def login_user(self, username, password):
		for user in users_list:
			if user['username'] == username and user['password'] == password:
				return {"message": "user {}, logged in successfully".format(username)}