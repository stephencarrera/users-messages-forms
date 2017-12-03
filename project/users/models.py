from project import db

class User(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	created_on = db.Column(db.DateTime, server_default=db.func.now())
	updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
	messages = db.relationship('Message', backref='user', lazy='dynamic', cascade='all, delete')

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def __repr__(self):
		return f"The user's name is {self.first_name} {self.last_name}"
