from flask import render_template, session, request, Blueprint
from flask_login import current_user, login_required
from robot.models import Message
import uuid

core = Blueprint('core', __name__)

@core.route('/')
def index():
	return render_template('index.html')

@core.route('/sent')
def sent():
	return render_template('sent.html')

@core.route('/messages')
def messages():
	messages = Message.query.all()
	return render_template('messages.html', messages=messages)