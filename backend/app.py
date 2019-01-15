# libraries
from flask import Flask
from flask_cors import CORS, cross_origin
import pymysql
from flask_sqlalchemy import SQLAlchemy
import os, sys
from dotenv import load_dotenv
from flask_jwt_extended import (JWTManager)
load_dotenv()

app = Flask(__name__)
app.config['JWT_TOKEN_LOCATION'] = ['query_string']
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)
CORS(app)
app.secret_key = 'test secret key'
ConnectionString = "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4" \
    % (os.getenv('DB_USER'),os.getenv('DB_PASSWORD'),os.getenv('DB_SERVER'),os.getenv('DB_PORT'),os.getenv('DB_NAME'))
app.config['SQLALCHEMY_DATABASE_URI'] = ConnectionString
db = SQLAlchemy(app)

#Models
from Models import *

db.create_all()


    