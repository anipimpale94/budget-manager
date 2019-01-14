# libraries
from flask import Flask, request, render_template, jsonify, session
from flask_cors import CORS, cross_origin
import pymysql
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# self made classes
# from User import User
from Portfolio import Portfolio

app = Flask(__name__)
CORS(app)
app.secret_key = 'test secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ringhell:qwerty94@db4free.net:3306/budget_manager?charset=utf8mb4'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    create_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % self.name

# db.create_all()

# temporary filesystem storage and will be replaced with DB soon #
# user table
# global user_id
# user_id = 0
# UserList = []
# tempUser = User(0, 'Ani', 'pimpale1994@gmail.com', 'qwerty') 
# UserList.append(tempUser)

# portfolio table
global portfolio_id
portfolio_id = 0
PortfolioList = []
tempPortfolio = Portfolio(0, 0, 'Repairs', 100)
PortfolioList.append(tempPortfolio)

# category table

# budget table
###

# function to check sessions
# @app.route("/", methods=['GET'])
# def index():
#     if request.method == 'GET':
#         if session.get('user_id') != None:
#             for user in UserList:
#                 if user.id == session.get('user_id'):
#                     return jsonify(Name=user.name, ID=user_id, message="Login Successful")
#             return jsonify(name="", id=-1, message="Not Logged In")
#         return jsonify(name="", id=-1, message="Not Logged In")
#     else:
#         return jsonify(error="Please use GET call")

# function to login user
@app.route("/login", methods=['POST'])
def login_request():   
    model = request.get_json(silent=True)
    if request.method == 'POST':
        # for user in UserList:
        #     if user.email == model.get('email'):
        #         if user.password == model.get('password'):
        #             session.clear()
        #             session['user_id'] = user_id
        #             print("login done",  session)
        #             print("login done",  session.get('user_id'))
        #             return jsonify(name=user.name, id=user_id, message="Login Successful")
        #         else:
        #             return jsonify(error="Incorrect Password")
        # return jsonify(error="Incorrect Login Details")
        user = User.query.filter_by(email=model.get('email')).first();
        if user != None:
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
        # user_id += 1
        # for user in UserList:
        #     if user.email == model.get('email'):
        #         return jsonify(error="User Already Exist")
        # new_user = User(user_id, model.get('name'), model.get('email'), model.get('password'))
        # UserList.append(new_user)
        # session.clear()
        # session['user_id'] = user_id
        # return jsonify(name=new_user.name, id=user_id,message="Registration Successful")
        user = User.query.filter_by(email=model.get('email')).first();
        if user == None:
            current_user = User(name=model.get('name'), email=model.get('email'), password=model.get('password'), create_date=datetime.now)
            print(current_user)
            db.session.add(current_user)
            db.session.commit()
            return jsonify(name=current_user.name, id=current_user.id, message="Registration Successful")
        else:
            return jsonify(error="User Already Exist")
    else:
        return jsonify(error="Please use POST call")

# function for log out
app.route("/logout", methods=['GET'])
def logout():
    session.clear()

# function for fetching budget portfolio
@app.route("/budget", methods=['GET'])
def get_budget_list(user_id):
    if request.method == 'GET':
        if session['user_id'] != None:
            Result = []
            for item in PortfolioList:
                if item.user_id == user_id:
                    Result.append(item)        
            return jsonify(message="Successful")
        else: 
            return jsonify(error="Please Login")
    return jsonify(error="Please use GET call")

# main call
if __name__ == '__main__':
    app.run(debug=True)
    