from flask import Blueprint, request, jsonify, json, abort
import datetime
# from api.auth import models
# from api.auth.utils import Validate
# later we shall need to put all the functions in this route in main utils model


auth = Blueprint('auth', __name__, url_prefix='api/v1')