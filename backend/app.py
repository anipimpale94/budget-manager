from flask import Flask, request, render_template, jsonify
import pandas as pd
from flask_cors import CORS, cross_origin
from User import User

app = Flask(__name__)

CORS(app)

# temporary filesystem storage and will be replaced with DB soon #
global user_id
user_id = 0
UserList = []
tempUser = User(0, 'Ani', 'pimpale1994@gmail.com', 'qwerty') 
UserList.append(tempUser)
###

@app.route("/")
def index():
    return ('', 204)

@app.route("/login", methods=['POST'])
def login_request():   
    model = request.get_json(silent=True)
    if request.method == 'POST':
        for user in UserList:
            if user.email == model.get('email'):
                if user.password == model.get('password'):
                    return jsonify(Name=user.name, Email=user.email)
                else:
                    return jsonify(error="Incorrect Password Detail")
        return jsonify(error="Incorrect Login Detail")
    else:
        return ('', 204)

@app.route("/register", methods=['POST'])
def register_request():
    model = request.get_json(silent=True)
    global user_id
    if request.method == 'POST':
        user_id += 1
        new_user = User(user_id, model.get('name'), model.get('email'), model.get('password'))
        UserList.append(new_user)
        return jsonify(error="Registration Successful")
    else:
        return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
