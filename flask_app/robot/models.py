# -*- coding: utf-8 -*-
from flask_app import db
from datetime import datetime
import json
import requests

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