import os
from config import Config #import the environment variables (not being user for now)

from flask import Flask, request, json
# import psycopg2

# db = somedb_to_be_used()
# bcrypt = Bcrypt() # encryption function
# creation of app into a function to create instance of our app with different
# configurations

def create_app(config_class=Config):
	app = Flask(__name__)

	app.config.from_object(Config)
	# import Auth and Main Blueprint instances in api folder 
	from api.auth.routes import auth
	from api.main.routes import main
	# register the blueprint
	app.register_blueprint(auth) 
	app.register_blueprint(main)

	# db.init_app(app) #we shall activate this later to incorporate DB
#   # bcrypt.init_app(app)

# create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # a simple page that says hello
#     @app.route('/hello')
#     def hello():
#         return 'Hello, World!'

	return app