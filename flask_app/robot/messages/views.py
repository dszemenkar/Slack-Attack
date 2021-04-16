from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from robot import db
from robot.models import Message
from robot.messages.forms import MessageForm

messages = Blueprint('messages', __name__)

@stories.route('/message/create', methods=['GET', 'POST'])
#@login_required
def create():
	form = MessageForm()

	#if current_user.admin == 0:
	#	abort(403)

	if form.validate_on_submit():
		message = Message(message=form.message.data,
							)
		#db.session.add(message)
		#db.session.commit()
		return redirect(url_for('core.sent'))
	return render_template('send_message.html', form=form)