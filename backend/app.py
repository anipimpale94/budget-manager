from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
from User import User
from Portfolio import Portfolio

app = Flask(__name__)

CORS(app)

# temporary filesystem storage and will be replaced with DB soon #
# user table
global user_id
user_id = 0
UserList = []
tempUser = User(0, 'Ani', 'pimpale1994@gmail.com', 'qwerty') 
UserList.append(tempUser)

# portfolio table
global portfolio_id
portfolio_id = 0
PortfolioList = []
tempPortfolio = Portfolio(0, 0, 'Repairs', 100)
PortfolioList.append(tempPortfolio)

# category table

# budget table
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
                    return jsonify(Name=user.name, ID=user_id, message="Login Successful")
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
        return jsonify(Name=new_user.name, ID=user_id,message="Registration Successful")
    else:
        return jsonify(error="Please use Post call")

@app.route("/budget/<user_id>", methods=['GET'])
def get_budget_list(user_id):
    if user_id != None:
        Result = []
        for item in PortfolioList:
            if item.user_id == user_id:
                Result.append(item)
        
        return(message="Successful")
    else: 
        return jsonify(error="Please Login")


if __name__ == '__main__':
    app.run(debug=True)
    