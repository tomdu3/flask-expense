from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import UserInputForm
from app.models import IncomeExpenses
from sqlalchemy import func, case

@app.route("/")
def index():
    entries = IncomeExpenses.query.order_by(
        IncomeExpenses.date.desc()
    ).all()
    
    # Use func.coalesce and func.sum instead of db.func
    total_amount = db.session.query(
        func.coalesce(
            func.sum(
                case(
                    (func.lower(IncomeExpenses.type) == 'income', IncomeExpenses.amount),
                    (func.lower(IncomeExpenses.type) == 'expense', -IncomeExpenses.amount),
                    else_=0
                )
            ),
            0.0
        )
    ).scalar()
    
    return render_template(
        "index.html",
        title="Transaction List",
        entries=entries,
        total_amount=total_amount
    )


@app.route("/add", methods=["GET", "POST"])
def add_expense():
    form = UserInputForm()
    if form.validate_on_submit():
        amount = form.amount.data
        if form.type.data == 'Expense':
            amount = -amount
        entry = IncomeExpenses(
            type=form.type.data,
            amount=amount,
            category=form.category.data,
            description=form.description.data,
        )
        try:
            db.session.add(entry)
            db.session.commit()
            flash("Entry added successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding entry: {e}", "danger")
        return redirect(url_for("index"))
    return render_template(
        "add.html",
        title="Add Expense/Income Entry",
        form=form
        )


@app.route("/flowbite-test")
def flowbite_test():
    return render_template("flowbite_test.html", title="Flowbite Test")

@app.route("/delete/<int:entry_id>")
def delete(entry_id):
    entry = IncomeExpenses.query.get_or_404(entry_id)
    try:
        db.session.delete(entry)
        db.session.commit()
        flash("Entry deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting entry: {e}", "danger")
    return redirect(url_for("index"))

@app.route("/edit/<int:entry_id>", methods=["GET", "POST"])
def edit(entry_id):
    entry = IncomeExpenses.query.get_or_404(entry_id)
    form = UserInputForm(obj=entry)
    if form.validate_on_submit():
        entry.type = form.type.data
        if entry.type == 'Expense':
            entry.amount = -form.amount.data
        else:
            entry.amount = form.amount.data
        entry.category = form.category.data
        entry.description = form.description.data
        try:
            db.session.commit()
            flash("Entry updated successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error updating entry: {e}", "danger")
        return redirect(url_for("index"))
    return render_template(
        "edit.html",
        title="Edit Expense/Income Entry",
        form=form
        )


@app.template_filter()
def number_format(
    value: float,
    decimal_places: int = 2,
    decimal_sep: str = '.',
    thousand_sep: str = ','
    ) -> str:
    """
    Format a number with a specified number of decimal places
    and thousand separator.
    
    Args:
        value (float): The number to format.
        decimal_places (int): The number of decimal places.
        decimal_sep (str): The decimal separator.
        thousand_sep (str): The thousand separator.
    
    Returns:
        str: The formatted number.
    """
    try:
        format_str = "{:,.{prec}f}".format(value, prec=decimal_places)
        if thousand_sep != ',':
            format_str = format_str.replace(',', thousand_sep)
        if decimal_sep != '.':
            format_str = format_str.replace('.', decimal_sep)
        return format_str
    except (ValueError, TypeError):
        return value
    

@app.route("/dashboard")
def dashboard():
    try:
        # Query for income vs expense totals
        income_vs_expense = db.session.query(
            db.func.sum(IncomeExpenses.amount),
            IncomeExpenses.type).group_by(
                IncomeExpenses.type
                ).order_by(
                    IncomeExpenses.type
                    ).all()
    except Exception as e:
        flash(f"Error fetching income vs expense data: {e}", "danger")
        income_vs_expense = []

    # Convert to JSON-serializable format
    income_vs_expense_data = [
        {"amount": float(amount) if amount else 0, 
         "type": type_}
        for amount, type_ in income_vs_expense
    ]

    try:
        # Query for income categories
        income_categories = db.session.query(
            db.func.sum(IncomeExpenses.amount),
            IncomeExpenses.category
        ).filter(
            IncomeExpenses.type == 'income'
        ).group_by(
            IncomeExpenses.category
        ).order_by(
            IncomeExpenses.category
        ).all()
    except Exception as e:
        flash(f"Error fetching income categories: {e}", "danger")
        income_categories = []

    # Convert income categories to JSON-serializable format
    income_category_data = [
        {"amount": float(amount) if amount else 0,
         "category": category}
        for amount, category in income_categories
    ]

    try:
        # Query for expense categories
        expense_categories = db.session.query(
            db.func.sum(IncomeExpenses.amount),
            IncomeExpenses.category
        ).filter(
            IncomeExpenses.type == 'expense'
        ).group_by(
            IncomeExpenses.category
        ).order_by(
            IncomeExpenses.category
        ).all()
    except Exception as e:
        flash(f"Error fetching expense categories: {e}", "danger")
        expense_categories = []

    # Convert expense categories to JSON-serializable format
    expense_category_data = [
        {"amount": float(amount) if amount else 0,
         "category": category}
        for amount, category in expense_categories
    ]

    try:
        # Query for dates
        dates = db.session.query(
            db.func.sum(IncomeExpenses.amount),
            IncomeExpenses.date
            ).group_by(
                IncomeExpenses.date
                ).order_by(
                    IncomeExpenses.date
                    ).all()
    except Exception as e:
        flash(f"Error fetching dates: {e}", "danger")
        dates = []
    
    # Convert to JSON-serializable format
    dates_data = [
        {"amount": float(amount) if amount else 0, 
         "date": date.strftime("%m-%d-%y")}
        for amount, date in dates
    ]

    # Extract lists for the template
    income_category = [item["amount"] for item in income_category_data]
    expense_category = [item["amount"] for item in expense_category_data]
    income_expense = [item["amount"] for item in income_vs_expense_data]
    over_time_expenditure = [item["amount"] for item in dates_data]
    dates_label = [item["date"] for item in dates_data]

    return render_template(
        "dashboard.html",
        title="Dashboard",
        income_vs_expense=income_vs_expense_data,
        income_categories=income_category_data,
        expense_categories=expense_category_data,
        dates=dates_data,
        income_category=income_category,
        expense_category=expense_category,
        income_expense=income_expense,
        over_time_expenditure=over_time_expenditure,
        dates_label=dates_label
        )