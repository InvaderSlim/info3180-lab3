from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField


class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField(
        'Name',
        [DataRequired()]
    )
    email = EmailField(
        'Email',
        [
            Email(message=('Not a valid email address.')),
            DataRequired()
        ]
    )
    subject = StringField(
        'Subject',
        [DataRequired()]
    )
    message = TextField(
        'Message',
        [
            DataRequired(),
        ]
    )
    submit = SubmitField('Submit')