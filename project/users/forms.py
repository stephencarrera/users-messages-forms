from flask_wtf import FlaskForm
from wtforms import StringField, validators

class UserForm(FlaskForm):
	first_name=StringField('First Name', [validators.DataRequired()],render_kw={"class":"col-4"})
	last_name=StringField('Last Name', [validators.DataRequired()],render_kw={"class":"col-4"})

class DeleteForm(FlaskForm):
	pass