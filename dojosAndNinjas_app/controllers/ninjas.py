from dojosAndNinjas_app import app
from flask import render_template, redirect, request
from dojosAndNinjas_app.models.ninja import Ninja
from dojosAndNinjas_app.models.dojo import Dojo

@app.route("/ninjas")
def ninjas():
    print("TEST1")
    dojos_all = Dojo.get_all()
    print("TEST2")
    return render_template("ninjas.html", dojos_all = dojos_all)

@app.route("/add_ninja", methods=["POST"])
def add_ninja():
    data = {
        "dojo_id" : request.form["dojo_id"],
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }
    new_ninja = Ninja.add_ninja( data )
    return redirect("/dojos")
    