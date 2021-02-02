from flask import Blueprint, render_template, redirect
from flask import request, jsonify, session

register = Blueprint('register', __name__, static_folder='static', static_url_path='/register', template_folder='templates')


def password_match(request):
    if request.args["rep_password"] == request.args["password"]:
        return True
    return False


@register.route('/login/register', methods=['GET', 'POST'])
def index(status=-1):
    if request.args:
        status = request.args["status"]
    return render_template('register.html', status=status)
