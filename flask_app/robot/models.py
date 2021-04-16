# -*- coding: utf-8 -*-
from robot import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
import json
import requests

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

class Message(db.Model):
	__tablename__ = 'messages'

	id = db.Column(db.Integer, primary_key=True)
	message = db.Column(db.String(), nullable=False)
	created = db.Column(db.String(), nullable=False)

	def __init__(self, message, created):
		self.message = message
		self.created = created

	def __repr__(self):
		return self.message

class User(db.Model, UserMixin):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	admin = db.Column(db.Integer, nullable=False, default=1)

	def __init__(self, email, username, password):
		self.email = email
		self.username = username
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return f'Username {self.username}'

