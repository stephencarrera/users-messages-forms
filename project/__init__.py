from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_modus import Modus
import os

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://localhost/umf-blueprints'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

modus = Modus(app)
db = SQLAlchemy(app)
Moment(app)



@app.errorhandler(404)
def page_not_found(error):
	return render_template('errors.html', error=error), 404