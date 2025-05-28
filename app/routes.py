from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import UserInputForm
from app.models import IncomeExpenses

@app.route("/")
def index():
    entries = IncomeExpenses.query.all()
    return render_template("index.html", entries=entries)


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

@app.route("/delete/<int:entry_id>")
def delete(entry_id):
    entry = IncomeExpenses.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted successfully!", "success")
    return redirect(url_for("index"))

@app.route("/edit/<int:entry_id>")
def edit(entry_id):
    entry = IncomeExpenses.query.get_or_404(entry_id)
    form = UserInputForm(obj=entry)
    if form.validate_on_submit():
        entry.type = form.type.data
        entry.amount = form.amount.data
        entry.category = form.category.data
        entry.description = form.description.data
        db.session.commit()
        flash("Entry updated successfully!", "success")
        return redirect(url_for("index"))
    return render_template("edit.html", title="Edit Expense/Income Entry", form=form)
