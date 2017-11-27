import os


class Config():
	# be sure to add a key variable in $VIRTUAL_ENV/bin/postactivate
	SECRET_KEY = os.environ.get('SECRET_KEY')
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'postgres://localhost/users-messages'
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	DEBUG = False


class DevelopmentConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgres://localhost/users-messages'
