from flask import Blueprint, render_template, redirect
from flask import request, jsonify, session, url_for
from pages.register.user import user

B4U = Blueprint('B4U', __name__, static_folder='static', static_url_path='/B4U', template_folder='templates')


@B4U.route('/', methods=['GET', 'POST'])
def index():
    pictures = [['images/Picture0.png', 'images/Picture5.png'],
                ['images/all_models (13).jpeg', 'images/long_sleeve (3).jpeg'],
                ['images/top_sales (5).jpeg', 'images/bikini (65).jpeg']]
    if request.method == 'POST':
        session['user'] = request.form['username']
        user_name, password = request.form["username"], request.form["password"]
        login_user = user(user_name, password)
        user_in_system = login_user.valid_login()
        if user_in_system == 2:
            return redirect(url_for('login.index', status=2))
        if user_in_system == 0:
            return redirect(url_for('login.index', status=0))
    else:
        session['user'] = 'אורח'
    return render_template('B4U.html', pictures=pictures, endpoint=request.endpoint)
