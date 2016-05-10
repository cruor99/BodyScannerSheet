from flask import Flask
from flask_restful import Resource, Api
from flask.ext.sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://" + config.user + ":" + config.password + "@" + config.database + "/" + config.schema
api = Api(app)
db = SQLAlchemy(app)

class Users(db.Model):
	__tablename__ = 'Users'
	user_id = db.Column(db.Integer, primary_key=True)
	user_email = db.Column(db.Text, nullable=False)
	user_name = db.Column(db.Text, nullable=False)
	user_password = db.Column(db.Text, nullable=False)
	user_start_date = db.Column(db.DateTime, default=db.func.current_timestamp())
	user_sex = db.Column(db.Text, nullable=True)
	user_age = db.Column(db.INTEGER, nullable=True)
	user_height = db.Column(db.INTEGER, nullable=True)


	def __init__(self, user_email, user_name, user_password):
		self.user_email = user_email
		self.user_name = user_name
		self.user_password = user_password

class Friend_List(db.Model):
	__tablename__ = 'Friend_List'
	user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), primary_key=True)
	friend_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
	friend_status = db.Column(db.Text, nullable=False) # Coach or Friend

	def __init__(self, user_id, friend_id, friend_status):
		self.user_id = user_id
		self.friend_id = friend_id
		self.friend_status = friend_status

class Scan(db.Model):
	__tablename__ = 'Scan'
	scan_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
	author_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
	scan_date = db.Column(db.DateTime, default=db.func.current_timestamp())
	user_comment = db.Column(db.Text)
	coach_comment = db.Column(db.Text)
	weight = db.Column(db.Float)
	bmi = db.Column(db.Float)
	fat_percentage = db.Column(db.Float)
	metabolism = db.Column(db.INTEGER)
	metabolic_age = db.Column(db.INTEGER)
	water_percentage = db.Column(db.Float)
	visceral_fat = db.Column(db.Float)
	bone_mass = db.Column(db.Float)
	muscle_mass = db.Column(db.Float)
	physical_score = db.Column(db.Float)

	def __init_(self, scan_id, user_id, author_id):
		self.scan_id = scan_id
		self.user_id = user_id
		self.author_id = author_id
