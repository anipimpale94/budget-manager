# libraries
from flask import request, jsonify
from time import gmtime, strftime
import datetime
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)

# self made
from app import app, db, jwt
from Models import *

# function for session check
@app.route("/api/session", methods=['GET'])
@jwt_required
def check_session():
    if request.method == 'GET':
        identity = get_jwt_identity()
        token = JWT.query.filter_by(token=request.args.get("jwt")).filter(JWT.expiry_date < datetime.datetime.now()).first()
        if token:
            user = User.query.filter_by(email=identity).first();
            access_token = token.token
            return jsonify(active="true", name=user.name, id=user.id, access_token=access_token, message="Login Successful")
        else:
            return jsonify(active="false", message="Invalid Token")
    else:     
        return
    

# function to login user
@app.route("/api/login", methods=['POST'])
def login_request():   
    model = request.get_json(silent=True)
    if request.method == 'POST':
        user = User.query.filter_by(email=model.get('email')).first();
        if user:
            access_token = create_access_token(identity=user.email)
            db.session.add(JWT(token=access_token, expiry_date=datetime.datetime.now() + datetime.timedelta(minutes=15)))
            db.session.commit()
            return jsonify(name=user.name, id=user.id, access_token=access_token, message="Login Successful")
        else:
            return jsonify(error="Incorrect Login Details")
    else:
        return jsonify(error="Please use POST call")

# function to register user and then login
@app.route("/api/register", methods=['POST'])
def register_request():
    model = request.get_json(silent=True)
    if request.method == 'POST':
        user = User.query.filter_by(email=model.get('email')).first();
        if user:
            return jsonify(error="User Already Exist")
        else:
            current_user = User(name=model.get('name'), email=model.get('email'), password=model.get('password'), create_date=gmtime())
            current_user.hash_password(current_user.password)
            db.session.add(current_user)
            access_token = create_access_token(identity=current_user.email)
            db.session.add(JWT(token=access_token, expiry_date=datetime.datetime.now() + datetime.timedelta(minutes=15)))
            db.session.commit()
            return jsonify(name=current_user.name, id=current_user.id, message="Registration Successful")         
    else:
        return jsonify(error="Please use POST call")

# function for log out
app.route("/api/logout", methods=['GET'])
def logout():
    session.clear()

# function for fetching budget portfolio
@app.route("/api/budget", methods=['GET'])
def get_budget_list():
    if request.method == 'GET':
        return jsonify(message="Successful")
    else:
        return jsonify(error="Please use GET call")

# main call
if __name__ == '__main__':
    app.run(debug=True)
    