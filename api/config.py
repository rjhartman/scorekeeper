import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

time.sleep(30)

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:idontcare@postgres/scorekeeper"

db = SQLAlchemy(app)
ma = Marshmallow(app)
