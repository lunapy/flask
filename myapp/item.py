from flask import Blueprint, render_template
from .models import Item

item_bp = Blueprint('item_bp', __name__)


@item_bp.route('/')
def get_items():
    items = Item.query.all()
    return render_template('item/index.html', items=items)