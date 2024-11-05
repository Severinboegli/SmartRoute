from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, TextAreaField
from wtforms.fields import DecimalField, SelectField, IntegerField, DateField
from wtforms import validators


class CustomerForm(FlaskForm):
    customerId = IntegerField("customerId", [validators.InputRequired()])
    firstname = StringField("firstname")
    name = StringField("name")
    plz = IntegerField("plz")
    city = StringField("city")
    phonenumber = StringField("phonenumber")
    customerSince = DateField("customerSince")
    