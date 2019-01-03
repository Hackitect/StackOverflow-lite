import os
from instance.config import app_config #import the environment variables
from flask import Flask, request, json
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
# import psycopg2
# from .api.v1 import version1 as v1
# db = somedb_to_be_used()
bcrypt = Bcrypt() # encryption function
# creation of app into a function to create instance of our app with different
# configurations

def create_app():
	app = Flask(__name__)
	# if test_config is None:
	# 	# load the instance config, if it exists, when not testing
	# 	app.config.from_pyfile('config.py', silent=True)
	# import Auth and Main Blueprint instances in api folder


	# to get big random characters, start python interpreter, import secrets module, then 
	# use secrets.token_hex() method and pass in 24bytes to genrate a random string 
	app.config['JWT_SECRET_KEY'] = '9a231f01574449fd12a4f4dcde53abb3a3d384cdb0367086'
	from app.api.v1.users.views import auth
	from app.api.v1.questions.views import questions
		
	# register the blueprint
	app.register_blueprint(auth) 
	app.register_blueprint(questions)

	# db.init_app(app) #we shall activate this later to incorporate DB
	bcrypt.init_app(app)
	jwt = JWTManager(app)
	return app
