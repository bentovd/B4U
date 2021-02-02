from flask import Blueprint, render_template, redirect
from flask import request, jsonify, session
from flask import url_for
from pages.register.user import user

login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')


def password_match(request):
    if request.form["rep_password"] == request.form["password"]:
        return True
    return False


@login.route('/login', methods=['GET', 'POST'])
def index(status=-1):
    if request.method == 'POST':
        user_name = request.form["username"]
        password = request.form["password"]
        new_user = user(user_name, password)
        if new_user.exist():
            return redirect(url_for('register.index', status=1))
        if not password_match(request):
            return redirect(url_for('register.index', status=2))
        else:
            new_user.add_to_db()
    if request.args:
        status = request.args["status"]
    return render_template('login.html', status=status)


@login.route('/log_out')
def log_out():
    session.pop('user')
    return redirect('/')


