# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
import enum


db = SQLAlchemy()

class Productline(db.Model):
    __tablename__ = 'productlines'

    productLine = db.Column(db.String(50), primary_key=True)
    textDescription = db.Column(db.String(4000))
    htmlDescription = db.Column(db.String)
    #image = db.Column(db.MEDIUMBLOB)



class Product(db.Model):
    __tablename__ = 'products'

    productCode = db.Column(db.String(15), primary_key=True)
    productName = db.Column(db.String(70), nullable=False)
    productLine = db.Column(db.ForeignKey('productlines.productLine'), nullable=False, index=True)
    productScale = db.Column(db.String(10), nullable=False)
    productVendor = db.Column(db.String(50), nullable=False)
    productDescription = db.Column(db.Text, nullable=False)
    quantityInStock = db.Column(db.SmallInteger, nullable=False)
    buyPrice = db.Column(db.Numeric(10, 2), nullable=False)
    MSRP = db.Column(db.Numeric(10, 2), nullable=False)

    productline = db.relationship('Productline', primaryjoin='Product.productLine == Productline.productLine', backref='products')
    
    
class Customer(db.Model):
    __tablename__ = "customers"
    
    customerId = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable = False)
    plz = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(15), nullable = False)
    phonenumber = db.Column(db.String(15), nullable = False)
    customerSince = db.Column(db.DateTime, nullable = False)
    
class PhilipsHue(db.Model):
    __tablename__ = "philipshue"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    ip = db.Column(db.String(20), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    farbe = db.Column(db.String(20), nullable=False)
    
class Nanoleaf(db.Model):
    __tablename__ = "nanoleaf"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    ip = db.Column(db.String(20), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    anzahlPanel = db.Column(db.Integer, nullable=False)
    
class NanoleafPanel(db.Model):
    __tablename__ = "nanoleafpanel"
    
    panelId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    hue = db.Column(db.Integer, nullable=False)
    saturation = db.Column(db.Integer, nullable=False)
    brightness = db.Column(db.Integer, nullable=False)
    nanoleafId = db.Column(db.Integer, db.ForeignKey('nanoleaf.id'), nullable=False)
    
    nanoleaf = db.relationship('Nanoleaf', primaryjoin='NanoleafPanel.nanoleafId == Nanoleaf.id', backref='nanoleafpanel')
    
class Raum(db.Model):
    __tablename__ = "raum"
    
    raumId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    
class Routine(db.Model):
    __tablename__ = "routine"
    
    routineID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    startingDate = db.Column(db.DateTime, nullable=False)
    actionJSON = db.Column(db.String(1000), nullable=False)
    
class Farbe(db.Model):
    __tablename__ = "farbe"
    
    farbeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    hexcode = db.Column(db.String(20), nullable=False)
