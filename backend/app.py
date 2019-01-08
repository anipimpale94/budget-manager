from flask import Flask, request, render_template, jsonify
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
                    return jsonify(Name=user.name, Email=user.email, message="Login Successful")
                else:
                    return jsonify(error="Incorrect Password")
        return jsonify(error="Incorrect Login Details")
    else:
        return jsonify(error="Please use Post call")

@app.route("/register", methods=['POST'])
def register_request():
    model = request.get_json(silent=True)
    global user_id
    if request.method == 'POST':
        user_id += 1
        for user in UserList:
            if user.email == model.get('email'):
                return jsonify(error="User Already Exist")
        new_user = User(user_id, model.get('name'), model.get('email'), model.get('password'))
        UserList.append(new_user)
        return jsonify(Name=new_user.name, Email=new_user.email, message="Registration Successful")
    else:
        return jsonify(error="Please use Post call")

if __name__ == '__main__':
    app.run(debug=True)
