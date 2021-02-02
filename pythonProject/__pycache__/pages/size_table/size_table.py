from flask import Blueprint, render_template, redirect
from flask import request, jsonify, session

size_table = Blueprint('size_table', __name__, static_folder='static', static_url_path='/size_table', template_folder='templates')


@size_table.route('/size_table', methods=['GET', 'POST'])
def index():
    return render_template('size_table.html', endpoint=request.endpoint)
