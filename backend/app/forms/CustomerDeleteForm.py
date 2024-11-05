from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators


class CustomerDeleteForm(FlaskForm):
    customerId = StringField("customerId", [validators.InputRequired()])