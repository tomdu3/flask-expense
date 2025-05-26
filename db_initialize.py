from app import db, app
from app.models import IncomeExpenses

with app.app_context():
    db.create_all()
    print("Database initialized")
    print("\n--------------------")
    print("Add Entries")
    print("\n--------------------")

    entry1 = IncomeExpenses(amount=1000, category="salary", description="Salary")
    entry2 = IncomeExpenses(amount=500, category="rent", description="Rent")
    entry3 = IncomeExpenses(amount=100, category="transport", description="Transport")

    print("\nEntries:")
    print(entry1)
    print(entry2)
    print(entry3)

    db.session.add(entry1)
    db.session.add(entry2)
    db.session.add(entry3)

    print("\n--------------------")
    print("\nEntries added")
    db.session.commit()

    print("\n--------------------")
    print("\nDatabase initialized")
    print("\n--------------------")
    print("\nAccess all entries")
    print("\n--------------------")
    print("\n")

    all_entries = IncomeExpenses.query.all()
    for entry in all_entries:
        print(entry)

    print("\n--------------------")
