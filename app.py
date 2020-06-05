from flask import Flask, render_template
from models import setup_db, db
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route("/")
    def home_view():
        # return "<h1>Hello, World!</h1>"
        return render_template('pages/home.html')

    return app

app = create_app()

if __name__ == '__main__':
    app.run()