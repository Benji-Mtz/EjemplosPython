from flask import Blueprint
from flask import render_template

page = Blueprint('page', __name__)

@page.app_errorhandler(404)
def page_not_found(error):
    # Retornar algun numero, cadena template o lo que sea seguido de un numero
    return render_template('errors/404.html'), 404

@page.route('/')
def index():
    return render_template('index.html',title='Index')

@page.route('/login')
def login():
    return render_template('auth/login.html', title='Login')
