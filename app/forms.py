from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    # add
    # author (string) validator should make this textbox required
    # message (string) validator should make this textbox required
    # submit (button) text should say 'Send' 
