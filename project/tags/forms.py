from flask_wtf import FlaskForm
from wtforms import TextField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from project.models import Message

class MultiCheckboxField(SelectMultipleField):
	widget = widgets.ListWidget(prefix_label=False)
	option_widget = widgets.CheckboxInput()

class TagForm(FlaskForm):
	text = TextField('Tags', validators=[DataRequired()])
	messages = MultiCheckboxField('Messages', coerce=int)
	
	def set_choices(self):
		self.messages.choices = [(m.id, m.content) for m in Message.query.all()]

class DeleteForm(FlaskForm):
	pass