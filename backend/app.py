from flask import Flask, request, render_template, jsonify
import pandas as pd
# from filter import filter_xls
# from email_service import email_service

app = Flask(__name__)

@app.route("/")
def index():
    return ('', 204)

@app.route("/login", methods=['POST'])
def login_request():
    return jsonify(
        username='a',
        email='a@gmail.com',
        id=1
    )

@app.route("/register", methods=['POST'])
def register_request():
    return jsonify(
        username='a',
        email='a@gmail.com',
        id=1
    )

# @app.route('/upload', methods=['POST'])
# def upload():
#     if request.method == 'POST':
#         f = request.files['file']
#         df = filter_xls(pd.read_excel(f))
#         email_service(df)
#         return render_template('index.html')
#     else:
#         return render_template('index.html')

if __name__ == '__main__':
    app.run()
