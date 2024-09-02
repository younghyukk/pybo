from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired


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