# libraries
from flask import request, jsonify, session
from time import gmtime, strftime

# self made
from app import app, db
from Models import *

# function to login user
@app.route("/login", methods=['POST'])
def login_request():   
    model = request.get_json(silent=True)
    if request.method == 'POST':
        user = User.query.filter_by(email=model.get('email')).first();
        if user:
            return jsonify(name=user.name, id=user.id, message="Login Successful")
        else:
            return jsonify(error="Incorrect Login Details")
    else:
        return jsonify(error="Please use POST call")

# function to register user and then login
@app.route("/register", methods=['POST'])
def register_request():
    model = request.get_json(silent=True)
    global user_id
    if request.method == 'POST':
        user = User.query.filter_by(email=model.get('email')).first();
        if user:
            return jsonify(error="User Already Exist")
        else:
            current_user = User(name=model.get('name'), email=model.get('email'), password=model.get('password'), create_date=gmtime())
            db.session.add(current_user)
            db.session.commit()
            db.session.close()
            return jsonify(name=current_user.name, id=current_user.id, message="Registration Successful")         
    else:
        return jsonify(error="Please use POST call")

# function for log out
app.route("/logout", methods=['GET'])
def logout():
    session.clear()

# function for fetching budget portfolio
@app.route("/budget", methods=['GET'])
def get_budget_list():
    if request.method == 'GET':
        return jsonify(message="Successful")
    else:
        return jsonify(error="Please use GET call")

# main call
if __name__ == '__main__':
    app.run(debug=True)
    