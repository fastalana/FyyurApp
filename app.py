import os

from flask import Flask, render_template
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_cors import CORS

from models import setup_db, db

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    # CORS(app)

    @app.route("/")
    def home_view():
        # return "<h1>Hello, World!</h1>"
        return render_template('pages/home.html')

    return app

app = create_app()

if __name__ == '__main__':
    app.run()