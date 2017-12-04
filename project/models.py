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


MessageTag = db.Table('message_tags',
	db.Column('message_id', db.Integer, db.ForeignKey('messages.id')),
	db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)

class Message(db.Model):

	__tablename__ = 'messages'

	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	created_on = db.Column(db.DateTime, server_default=db.func.now())
	updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	tags = db.relationship('Tag', secondary=MessageTag, backref=db.backref('messages'))

	def __init__(self, content, user_id):
		self.content = content
		self.user_id = user_id


class Tag(db.Model):

	__tablename__ = 'tags'

	id = db.Column(db.Integer, primary_key=True)
	text= db.Column(db.Text)

	def __init__(self, text):
		self.text = text