from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import UserInputForm
from app.models import IncomeExpenses

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_expense():
    form = UserInputForm()
    if form.validate_on_submit():
        entry = IncomeExpenses(
            type=form.type.data,
            amount=form.amount.data,
            category=form.category.data,
            description=form.description.data,
        )
        db.session.add(entry)
        db.session.commit()
        flash("Entry added successfully!", "success")
        return redirect(url_for("index"))
    return render_template("add.html", title="Add Expense/Income Entry", form=form)


@app.route("/flowbite-test")
def flowbite_test():
    return render_template("flowbite_test.html", title="Flowbite Test")
