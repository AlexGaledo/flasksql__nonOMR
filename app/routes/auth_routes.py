from flask import Blueprint, jsonify, render_template, request
from ..db.database import create_table, sign_up

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/', methods=['GET'])
def default_response():
    create_table()
    return render_template('index.html')

#sign-up route
@auth_bp.route('/sign-up',methods=['POST'])
def sign_up():
    data = request.get_json()
    username = data.username
    password = data.password
    #better put error handling in db
    sign_up(username, password)
     

#sign-in route 
@auth_bp.route('/sign-in/:user_id', methods=['POST'])
def sign_in(user_id):
    data = request.get_json()
    id = user_id
    username = data.username
    password = data.password
    #call db function
    return render_template('index.html')






