from flask import render_template, session, request, Blueprint
from flask_app.models import Messages
import uuid

core = Blueprint('core', __name__)

@core.route('/')
def index():
	messages = Messages.query.all()

	return render_template('index.html', messages=messages)