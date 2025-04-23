from flask import Blueprint, jsonify, request
from website.models import *
from .. import db

classroom_bp = Blueprint('classroom_bp', __name__)

@classroom_bp.route('/classroom', methods = ['GET'])
def get_students():
    # print("hello world")
    pass