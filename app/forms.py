from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, validators
from wtforms.validators import DataRequired, Email

class ContactForm (FlaskForm):
    name = StringField('Name (Required)',validators=[DataRequired()])
    email =StringField('Email (Required)',validators=[DataRequired(), validators.email()])
    sub = StringField('Subject (Required)',validators=[DataRequired()])
    message = StringField('Message (Required)',validators=[DataRequired()])
    submit = SubmitField('Send')
