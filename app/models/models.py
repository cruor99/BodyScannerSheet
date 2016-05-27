#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
import bcrypt
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
import datetime

base = declarative_base()
engine = create_engine("mysql://" + config.user + ":" + config.password + "@" + config.database + "/" + config.schema, echo=True)
Session = sessionmaker(bind=engine)
db = Session()

class Users(base):
	__tablename__ = 'Users'
	user_id = Column(Integer, primary_key=True)
	user_email = Column(String(255), nullable=False)
	user_name = Column(String(255), nullable=False)
	user_password = Column(String(255), nullable=False)
	user_start_date = Column(DateTime, default=datetime.datetime.now)
	user_sex = Column(String(255), nullable=True)
	user_age = Column(Integer, nullable=True)
	user_height = Column(Integer, nullable=True)

	def checkPassword(self, password):
		if bcrypt.hashpw(password.encode('UTF-8'), self.user_password) == self.user_password:
			return True
		else:
			return False

	def __init__(self, user_email, user_name, user_password):
		self.user_email = user_email
		self.user_name = user_name
		self.user_password = bcrypt.hashpw(user_password.encode('UTF-8'), bcrypt.gensalt())

	def __repr__(self):
		return "<User(id='%s', email='%s', name='%s', password='%s', \
		startdate='%s', sex='%s', age='%s', height='%s')>" % (self.user_id, \
		self.user_email, self.user_name, self.user_password, self.user_start_date, \
		self.user_sex, self.user_age, self.user_height)

class Friend_List(base):
	__tablename__ = 'Friend_List'
	user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
	friend_id = Column(Integer, ForeignKey('Users.user_id'))
	friend_status = Column(String(255), nullable=False) # Coach or Friend

	def __init__(self, user_id, friend_id, friend_status):
		self.user_id = user_id
		self.friend_id = friend_id
		self.friend_status = friend_status

class Scan(base):
	__tablename__ = 'Scan'
	scan_id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
	author_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
	scan_date = Column(DateTime, default=datetime.datetime.now)
	user_comment = Column(String(255))
	coach_comment = Column(String(255))
	weight = Column(Float)
	bmi = Column(Float)
	fat_percentage = Column(Float)
	metabolism = Column(Integer)
	metabolic_age = Column(Integer)
	water_percentage = Column(Float)
	visceral_fat = Column(Float)
	bone_mass = Column(Float)
	muscle_mass = Column(Float)
	physical_score = Column(Float)

	def __init_(self, scan_id, user_id, author_id):
		self.scan_id = scan_id
		self.user_id = user_id
		self.author_id = author_id
