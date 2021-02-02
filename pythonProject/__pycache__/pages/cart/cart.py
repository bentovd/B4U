from flask import Blueprint, render_template, redirect
from flask import request, jsonify, session
from pages.contact.request2 import request2
from pages.register.user import user
from pages.swimsuits.model import model
from utilities.db.db_manager import dbManager as db

cart = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')



@cart.route('/cart', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user.delete_order(request.form, session["user"])
    orders, total_cart = user.get_orders(session["user"])
    return render_template('cart.html', orders=orders, total_cart=total_cart)


@cart.route('/cart/payment', methods=['GET', 'POST'])
def func():
    user_name = session["user"]
    orders, total_cart = user.get_orders(user_name)
    num_of_misses = model.update_models_values(orders, user_name)
    if num_of_misses > 0:
        return "WE DIDNT CREATE THIS PAGE.      \n IN OUR ASSAMPTIONS        \n חלק מהפריטים חסרים במלאי. חזרו לעגלה לצפייה בפריטים שלא נרכשו"
    return "WE DIDNT CREATE THIS PAGE. \n       IN OUR ASSAMPTIONS"