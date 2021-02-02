from flask import Blueprint, render_template, redirect
from flask import request, jsonify, session
from utilities.db.db_manager import dbManager as db
from pages.swimsuits.model import model
from pages.register.user import user
from pages.swimsuits.model import model

swimsuits = Blueprint('swimsuits', __name__, static_folder='static', static_url_path='/swimsuits', template_folder='templates')


def fetch_models(request, category):
    if request.args and request.method == 'GET':
        color, max_price, min_price, size = request.args["color"], request.args["max"], request.args["min"], \
                                            request.args["size"]
        models = model(category, color, max_price, min_price, size).models_selected
    else:
        models = model(category).models_selected
    return models

@swimsuits.route('/swimsuits', methods=['GET', 'POST'])
def index():
    categories = [['swimsuits.all_models', 'pictures/all_models/all_models (3).jpeg', 'all_models.html',  'כל הדגמים'],
                 ['swimsuits.full_body', 'pictures/full_body/full_body (2).jpeg', 'full_body.html', 'שלמים'],
                 ['swimsuits.bikini', 'pictures/bikini/bikini (16).jpeg', 'bikini.html', 'ביקיני'],
                 ['swimsuits.long_sleeve', 'pictures/long_sleeve/long_sleeve (3).jpeg', 'long_sleeve.html', 'שרוול ארוך'],
                 ['swimsuits.top_sales', 'pictures/top_sales/top_sales (6).jpeg', 'top_sales.html', 'הכי נמכרים']]
    return render_template('swimsuits.html', categories=categories, endpoint=request.endpoint)


@swimsuits.route('/swimsuits/all_models', methods=['GET', 'POST'])
def all_models():
    models = fetch_models(request, '%')
    return render_template('all_models.html', models=models, category='/swimsuits/all_models', endpoint='swimsuits.index')


@swimsuits.route('/swimsuits/bikini', methods=['GET', 'POST'])
def bikini():
    models = fetch_models(request, 'bikini')
    return render_template('bikini.html', models=models, category='/swimsuits/bikini', endpoint='swimsuits.index')


@swimsuits.route('/swimsuits/full_body', methods=['GET', 'POST'])
def full_body():
    models = fetch_models(request, 'full_body')
    return render_template('full_body.html', models=models, category='/swimsuits/full_body', endpoint='swimsuits.index')


@swimsuits.route('/swimsuits/long_sleeve', methods=['GET', 'POST'])
def long_sleeve():
    models = fetch_models(request, 'long_sleeve')
    return render_template('long_sleeve.html', models=models, category='/swimsuits/long_sleeve', endpoint='swimsuits.index')


@swimsuits.route('/swimsuits/top_sales', methods=['GET', 'POST'])
def top_sales():
    models = fetch_models(request, 'top_sales')
    return render_template('top_sales.html', models=models, category='/swimsuits/top_sales', endpoint='swimsuits.index')


@swimsuits.route('/swimsuits/buy_page/<int:makat>', methods=['GET', 'POST'])
def buy_page(makat):
    selected_model = model.featch_model(makat)
    temp_user = user(session['user'],'1234')
    if request.method == 'POST':
        temp_user.add_item(selected_model[0], request)
        return render_template('buy_page.html', model=selected_model[0], add=True)
    return render_template('buy_page.html', model=selected_model[0], endpoint='swimsuits.index')


