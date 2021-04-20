from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'

@app.route('/', methods=['GET', 'POST'])
def home():
    form=MessageForm()
    if form.validate_on_submit():
        # check if user exits in database
        # if not create user and add to database
        # create row in Message table with user (created/found) add to ta database
        user = User.query.filter_by(author= form.author.data).first()
        if user is None:
            new_user = User(author = form.author.data)
            db.session.add(new_user)
           
        new_message = Messages(message =form.message.data, user_id = User.query.filter_by(author = form.author.data).first().id)
        db.session.add(new_message)
        db.session.commit()

    posts = [
        {
            'author':'Carlos',
            'message': 'Yo! Where you at?!'

        },
        {
            'author':'Jerry',
            'message':'Home. You?'
        }
    ]
    # output all messages
    # create a list of dictionaries with the following structure
    # [{'author':'Carlos', 'message':'Yo! Where you at?!'},
    #  {'author':'Jerry', 'message':'Home. You?'}]

    every_message = Messages.query.all()
    if every_message is not None:
        for a_message in every_message:
            posts = posts + [
                {
                    'author': f'{User.query.filter_by(id = a_message.user_id).first().author}',
                    'message': f'{a_message.message}'

                }
            ]

    return render_template('home.html', posts=posts, form=form)

