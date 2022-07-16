import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    PWD = os.getenv('PWD')
    USR = os.getenv('USR')
    DB = os.getenv('DB')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USR}:{PWD}@localhost/{DB}'
    db.init_app(app)

    return app
    