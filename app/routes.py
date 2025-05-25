from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/layout")
def base():
    return render_template("base.html", title="Layout")


@app.route("/flowbite-test")
def flowbite_test():
    return render_template("flowbite_test.html", title="Flowbite Test")
