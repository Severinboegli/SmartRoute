from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, TextAreaField
from wtforms.fields import DecimalField, SelectField, IntegerField, DateField
from wtforms import validators


class NanoleafForm(FlaskForm):
    id = IntegerField("id", [validators.InputRequired()])
    name = StringField("name")
    ip = StringField("ip")
    port = IntegerField("port")
    panelCount = IntegerField("panelCount")

class PhilipshueForm(FlaskForm):
    id = IntegerField("id", [validators.InputRequired()])
    name = StringField("name")
    ip = StringField("ip")
    port = IntegerField("port")
    farbe = StringField("farbe")