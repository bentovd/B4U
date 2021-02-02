from flask import Blueprint, render_template, redirect
from flask import request, jsonify, session
from pages.contact.request2 import request2

contact = Blueprint('contact', __name__, static_folder='static', static_url_path='/contact', template_folder='templates')


@contact.route('/contact', methods=['GET', 'POST'])
def index():
    if request.form:
        name, last_name, email, phone, req = request.form["name"], request.form["Lname"], request.form["mail"], \
                                             request.form["phone"], request.form["req"]
        r=request2(name, last_name, email, phone, req)
        sent=True
    else: sent=False
    return render_template('contact.html', sent=sent, endpoint=request.endpoint)
