from dojosAndNinjas_app import app
from flask import render_template, redirect, request
from dojosAndNinjas_app.models.ninja import Ninja
from dojosAndNinjas_app.models.dojo import Dojo

@app.route("/ninjas")
def ninjas():
    dojos_all = Dojo.get_all()
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
    return redirect(f"/dojo_ind/{request.form['dojo_id']}")
    
    