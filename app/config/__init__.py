from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('KEY')
    app.config['DEBUG'] = os.getenv('DEBUG')

    '''Blueprints'''
    from app.routes.route import home
    app.register_blueprint(home)

    return app
