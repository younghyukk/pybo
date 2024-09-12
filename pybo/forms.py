from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField(
        label='subject',
        validators=[DataRequired('Subject is mandatory')]
    )

    content = TextAreaField(
        label='content',
        validators=[DataRequired('Content is mandatory')]
    )

class AnswerForm(FlaskForm):
    content = TextAreaField(
        label='content',
        validators=[DataRequired('Content is mandatory in the Answer Section')]
    )

class UserCreateForm(FlaskForm):
    username = StringField('User Name', validators=[
        DataRequired(), Length(min=3, max=25)
    ])
    password1 = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', 'Password does not match')
    ])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    email = EmailField('Email', [DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('User Name', validators=[
        DataRequired(), Length(min=3, max=25)
    ])
    password = PasswordField('Password', validators=[
        DataRequired()
    ])