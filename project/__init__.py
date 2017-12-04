from flask import Flask, redirect, url_for, render_template
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
import os

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://localhost/umf-blueprints'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

modus = Modus(app)
moment = Moment(app)
db = SQLAlchemy(app)


from project.users.views import users_blueprint
from project.messages.views import messages_blueprint
from project.tags.views import tags_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')
app.register_blueprint(tags_blueprint, url_prefix='/tags')

@app.route('/')
def root():
	return redirect(url_for('users.index'))


@app.errorhandler(404)
def page_not_found(error):
	return render_template('errors.html', error=error), 404

@app.errorhandler(500)
def server_error(error):
	return render_template('errors.html', error=error), 500