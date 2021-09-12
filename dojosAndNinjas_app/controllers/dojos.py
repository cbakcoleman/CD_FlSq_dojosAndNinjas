from dojosAndNinjas_app import app
from flask import render_template, redirect, request
from dojosAndNinjas_app.models.dojo import Dojo

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos", methods=[ "GET", "POST" ])
def dojos():
    if request.method == "POST":
        data = {
            "name" : request.form["name"]
        }
        new_dojo = Dojo.add_dojo( data )
        return redirect("/")
    else:
        dojos_all = Dojo.get_all()
        return render_template("dojos.html", dojos_all = dojos_all)

@app.route("/ind_dojo/<int:id>")
def dojo_ind(id):
    dojo = Dojo.dojo_ind({"id" : id })
    return render_template("dojo_ind.html", dojo = dojo)