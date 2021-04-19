from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from datetime import datetime
from robot import db
from robot.models import Message
from robot.messages.forms import MessageForm

messages = Blueprint('messages', __name__)

def getCreated():
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

@messages.route('/messages/create', methods=['GET', 'POST'])
#@login_required
def create():
	form = MessageForm()

	#if current_user.admin == 0:
	#	abort(403)

	if form.validate_on_submit():
		from datetime import datetime
		message = Message(message=form.message.data,
						  created=getCreated())
		#db.session.add(message)
		#db.session.commit()
		return redirect(url_for('core.sent'))
	return render_template('send_message.html', form=form)

@messages.route('/messages/<int:message_id>')
def message(message_id):
	message = Message.query.get_or_404(message_id)
	return render_template('message.html', message=message)