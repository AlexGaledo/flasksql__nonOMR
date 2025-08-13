from .session import engine
from sqlalchemy import text
from flask import jsonify
from flask_bcrypt import generate_password_hash, check_password_hash


#connection.execute for executing sql syntax
#connection.commit for committing

#CREATE TABLE IF NOT EXISTS
def initialize_table():
    with engine.connect() as connection:
        connection.execute(text("CREATE TABLE IF NOT EXISTS users "
        "(id INT AUTO_INCREMENT PRIMARY KEY," \
        " username VARCHAR(50), password VARCHAR(50))"))
        
        connection.execute(text(
            "ALTER TABLE users MODIFY password VARCHAR(255)"))

#sign-up
def sign_up(username,password):
    try:
        hashed_password = generate_password_hash(password).decode('utf-8')
        with engine.begin() as connection:
            connection.execute(text(
            "INSERT INTO users (username, password) VALUES (:username,:password)"),
            {"username":username,"password":hashed_password})
    except Exception as e:
        return jsonify({'response':f'error{e}'}),404

#sign-in
def sign_in(username,password):
    try: 
        user = find_user(username)
        stored_password = user['password']
        if check_password_hash(stored_password,password):
            return jsonify({'id':user['id'], 'username':user['username']})
    except Exception as e:
        return jsonify({'response':f'error:{e}'}),404
    
#change password
def change_password(username,new_password):
    try:
        hashed_password = generate_password_hash(new_password).decode('utf-8')
        with engine.connect() as connection:
            connection.execute(text(
                "UPDATE users SET password = :new_password " \
                "WHERE username = :username"),
                {"new_password":hashed_password,"username":username})
        return jsonify({"response":"password updated"}),200
    except Exception as e:
        return jsonify({'response':f'error:{e}'})

#delete user
def delete_user(username):
    try:
        user = find_user(username)
        with engine.connect() as connection:
            connection.execute(text(
                "DELETE FROM users " \
                "WHERE username = :username"),
            {'username':username})
        return jsonify({"response":"user deleted"}),200
    except Exception as e:
        return jsonify({"response":f"error{e}"})    
    
#utils
#fetchall / fetchone 
#results returns graph points
def find_user(username):
    with engine.connect() as connection:
         result = connection.execute(text(
            "SELECT * FROM users " \
            "WHERE username = :username"),
            {"username":username})
         
         row = result.mappings().fetchone()
         return row if row else False
    


    



      
      




