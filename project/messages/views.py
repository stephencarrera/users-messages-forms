from flask import Blueprint, render_template, redirect, request, url_for, flash
from project.models import User, Message
from project.messages.forms import MessageForm, DeleteForm
from project import db


messages_blueprint = Blueprint(
	'messages',
	__name__,
	template_folder = 'templates'
)

@messages_blueprint.route('/', methods=["GET", "POST"])
def index(user_id):
	delete_form = DeleteForm()
	if request.method == "POST":
		form = MessageForm(request.form)
		if form.validate():
			new_message=Message(request.form['content'], user_id)
			db.session.add(new_message)
			db.session.commit()
			flash('Message Created!')
			return redirect(url_for('messages.index', user_id=user_id))
		return render_template('new.html', user=User.query.get(user_id), form=form)	
	return render_template('index.html', user=User.query.get(user_id), form=delete_form)

@messages_blueprint.route('/new')
def new(user_id):
	message_form = MessageForm()
	return render_template('new.html', user=User.query.get(user_id), form=message_form)

@messages_blueprint.route('/<int:id>/edit')
def edit(user_id, id):
	message=Message.query.get_or_404(id)
	form = MessageForm(obj=message)
	return render_template('edit.html', message=message, form=form)

@messages_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(user_id, id):
	message=Message.query.get_or_404(id)
	if request.method == b'PATCH':
		form = MessageForm(request.form)
		if form.validate():
			time = db.func.now()
			message.updated_on = time
			message.content = request.form['content']
			db.session.add(message)
			db.session.commit()
			flash('Message Updated!')
			return redirect(url_for('messages.index', user_id=user_id))
		return render_template('edit.html', message=message, form=form)
	if request.method == b'DELETE':
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(message)
			db.session.commit()
			flash('Message Deleted!')
			return redirect(url_for('messages.index', user_id=user_id))
	return render_template('show.html', message=message)