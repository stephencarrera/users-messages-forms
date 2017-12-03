from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

class MessageForm(FlaskForm):
	content=TextAreaField('Content', [validators.DataRequired(), validators.length(max=280)], render_kw={"rows": 3, "cols": 30})

class DeleteForm(FlaskForm):
	pass
