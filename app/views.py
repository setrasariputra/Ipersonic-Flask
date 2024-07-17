from flask import Blueprint, render_template
from .controllers import get_user, ping

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    user = get_user('setrasariputra')
    return render_template('index.html', user=user)

@main_blueprint.route('/ping')
def ping():
    return render_template('ping.html')
