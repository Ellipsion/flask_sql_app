from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# app
app = Flask(__name__)

# db config
db_uri = os.getenv("MYSQL_URL")
db_config_key = "SQLALCHEMY_DATABASE_URI"
app.config[db_config_key] = db_uri

# initialize database
db = SQLAlchemy(app)

# Create db model


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variable = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())


@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        id = 1  # get the variable by id=1
        test = Test.query.get(id)
        return f"{test.variable} {test.date_created}"
    else:
        return "This is a GET only API."


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
