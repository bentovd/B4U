from flask import Blueprint, render_template, redirect
from flask import request, jsonify, session
from pages.contact.request2 import request2

cart = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')


@cart.route('/cart', methods=['GET', 'POST'])
def index():
    return 'cart_page'
