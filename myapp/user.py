from flask import Blueprint, render_template
from .models import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def user_home():
    users = User.query.all()
    return render_template('user/index.html', users=users)