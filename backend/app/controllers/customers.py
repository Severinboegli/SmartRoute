import sqlalchemy
import sqlalchemy.orm

from flask import redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
from model.models import Customer, db
from forms.CustomerDeleteForm import CustomerDeleteForm
from forms.CustomerForm import CustomerForm

customers_blueprint = Blueprint('customers_blueprint', __name__)

@customers_blueprint.route("/customers")
def customers():
    # workaround für sesssion Autocomplete
    session: sqlalchemy.orm.Session = db.session

    # alle products laden
    customers = session.query(Customer).order_by(Customer.customerId).all()

    return render_template("customers/customers.html", customers=customers)


#! Add Customers
@customers_blueprint.route("/customers/add", methods=["GET", "POST"])
def customers_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    add_customers_form = CustomerForm()

    if request.method == 'POST':

        if add_customers_form.validate_on_submit():
            # hier in db einfügen
            new_customer = Customer()
            
            new_customer.firstname = add_customers_form.firstname.data
            new_customer.name = add_customers_form.name.data
            new_customer.plz = add_customers_form.plz.data
            new_customer.city = add_customers_form.plz.data
            new_customer.phonenumber = add_customers_form.phonenumber.data
            new_customer.customerSince = add_customers_form.customerSince.data

            db.session.add(new_customer)
            db.session.commit()

            return redirect("/customers")
        else:
            return render_template("customers/customers_add.html", form=add_customers_form)
    else:
        return render_template("customers/customers_add.html", form=add_customers_form)





@customers_blueprint.route("/customers/edit", methods=["GET", "POST"])
def customers_edit():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_customer_form = CustomerForm()

    customer_Id = request.args["id"]

    # item laden (wie kann man einen datensatz lesen)
    customer_to_edit = session.query(Customer).filter(
        Customer.customerId == customer_Id).first()


    if request.method == "POST":
        if edit_customer_form.validate_on_submit():
            customer_Id = edit_customer_form.customerId.data
            customer_to_edit = db.session.query(Customer).filter(
                Customer.customerId == customer_Id).first()
            
            customer_to_edit.customerId = edit_customer_form.customerId.data
            customer_to_edit.firstname = edit_customer_form.firstname.data
            customer_to_edit.name = edit_customer_form.name.data
            customer_to_edit.plz = edit_customer_form.plz.data
            customer_to_edit.city = edit_customer_form.city.data
            customer_to_edit.phonenumber = edit_customer_form.phonenumber.data
            customer_to_edit.customerSince = edit_customer_form.customerSince.data

            db.session.commit()
        return redirect("/customers")
    else:
        edit_customer_form.customerId.data = customer_to_edit.customerId
        edit_customer_form.firstname.data = customer_to_edit.firstname
        edit_customer_form.name.data = customer_to_edit.name
        edit_customer_form.plz.data = customer_to_edit.plz
        edit_customer_form.city.data = customer_to_edit.city
        edit_customer_form.phonenumber.data = customer_to_edit.phonenumber
        edit_customer_form.customerSince.data = customer_to_edit.customerSince

        print("ERROR!!!!!: " + str(edit_customer_form.customerId))

        return render_template("customers/customers_edit.html", form=edit_customer_form)


@customers_blueprint.route("/customers/delete", methods=["post"])
def deleteCustomers():
    delete_item_form_obj = CustomerDeleteForm()
    if delete_item_form_obj.validate_on_submit():

        customer_code_to_delete = delete_item_form_obj.customerId.data
        customer_to_delete = db.session.query(Customer).filter(
            Customer.customerId == customer_code_to_delete)
        customer_to_delete.delete()

        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"Customer with id {customer_code_to_delete} has been deleted")

    return redirect("/customers")