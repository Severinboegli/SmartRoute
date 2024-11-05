import sqlalchemy
import sqlalchemy.orm

from flask import redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
from model.models import Nanoleaf, db, PhilipsHue

devices_blueprint = Blueprint('devices_blueprint', __name__)

@devices_blueprint.route("/devices")
def devices():
    session: sqlalchemy.orm.Session = db.session
    
    nanoleafs = session.query(Nanoleaf).order_by(Nanoleaf.id).all()
    hues = session.query(PhilipsHue).order_by(PhilipsHue.id).all()
    
    return render_template("devices/devices.html", nanoleafs=nanoleafs, hues=hues)


