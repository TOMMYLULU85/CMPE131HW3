from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    # add
    # author (string) validator should make this textbox required
    author = StringField('author', validators=[DataRequired()])
    # message (string) validator should make this textbox required
    message = StringField('message',validators=[DataRequired()])
    # submit (button) text should say 'Send' 
    submit = SubmitField('Send')

  