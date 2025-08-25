from flask import Blueprint, jsonify, render_template, request
from ..db.database import initialize_table, sign_up, sign_in

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/', methods=['GET'])
def default_response():
    initialize_table()

#sign-up route
@auth_bp.route('/sign-up',methods=['POST'])
def sign_up_route():
    data = request.get_json()
    username = data['username']
    password = data['password']
    #better put error handling in db
    sign_up(username, password)
    return jsonify({"response": "User created successfully!"}), 201
     

#sign-in route 
@auth_bp.route('/sign-in', methods=['POST'])
def sign_in_route():
    data = request.get_json()
    username = data['username']
    password = data['password']
    #call db function
    res = sign_in(username,password)
    return jsonify(res),200






