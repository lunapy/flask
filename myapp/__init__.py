from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from .user import user_bp
from .item import item_bp

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(item_bp, url_prefix='/item')
