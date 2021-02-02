from flask import url_for, Flask, render_template, redirect
from flask import request, session
from pages.B4U.B4U import B4U
from pages.login.login import login
from pages.register.register import register
from pages.contact.contact import contact
from pages.size_table.size_table import size_table
from pages.swimsuits.swimsuits import swimsuits
from pages.cart.cart import cart
from components.main_menu import main_menu


app = Flask(__name__)
app.secret_key = '12345'


app.register_blueprint(B4U)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(contact)
app.register_blueprint(size_table)
app.register_blueprint(swimsuits)
app.register_blueprint(cart)
app.register_blueprint(main_menu)




if __name__ == '__main__':
    app.run(debug=True)
