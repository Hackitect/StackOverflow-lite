from flask import Blueprint
from app.api.v1.questions import models
import datetime

questions = Blueprint('questions', __name__, url_prefix='/api/v1')


qu_object = models.Questions()


@questions.route("/api/v1/auth/questions", methods=['GET'])
def get_question():
	return jsonify(qu_object.get_all())