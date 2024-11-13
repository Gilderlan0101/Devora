from flask import render_template, Blueprint
home = Blueprint('home', __name__, template_folder='../templates')


@home.route("/devora/")
def home_page():
    return render_template('home.html')