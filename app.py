import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_definitions")
def get_definitions():
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 6
    offset = (page - 1) * 6
    total = mongo.db.definitions.find().count()
    definition = list(mongo.db.recipes.find())
    definition_paginated = definition[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap5')
    # definitions = list(mongo.db.definitions.find())
    return render_template("glossary.html", definitions=definition_paginated, page=page, per_page=per_page, pagination=pagination)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    definitions = list(
        mongo.db.definitions.find({"$text": {"$search": query}}))
    return render_template("glossary.html", definitions=definitions)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        redirect(url_for("dashboard", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "dashboard", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/dashboard<username>", methods=["GET", "POST"])
def dashboard(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("dashboard.html", username=username)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/homepage")
def homepage():
    return render_template("homepage.html")


@app.route("/add_definition", methods=["GET", "POST"])
def add_definition():
    if request.method == "POST":
        definition = {
            "category_name": request.form.get("category_name"),
            "definition_name": request.form.get("definition_name"),
            "definition_description": request.form.get(
                "definition_description"),
            "created_by": session["user"]
        }
        mongo.db.definitions.insert_one(definition)
        flash("Definition successfully added!")
        return redirect(url_for("get_definitions"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_definition.html", categories=categories)


@app.route("/edit_definition/<definition_id>", methods=["GET", "POST"])
def edit_definition(definition_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "definition_name": request.form.get("definition_name"),
            "definition_description": request.form.get(
                "definition_description"),
            "created_by": session["user"]
        }
        mongo.db.definitions.update({"_id": ObjectId(definition_id)}, submit)
        flash("Definition successfully edited!")

    definition = mongo.db.definitions.find_one(
        {"_id": ObjectId(definition_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_definition.html", definition=definition, categories=categories)


@app.route("/delete_definition/<definition_id>")
def delete_definition(definition_id):
    mongo.db.definitions.remove({"_id": ObjectId(definition_id)})
    flash("Definition deleted")
    return redirect(url_for("get_definitions"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
