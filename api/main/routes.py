from flask import Blueprint

main = Blueprint('main', __name__)


@main.route("/")
def home():
	return 'different APIs for the StackOverFlow project'
