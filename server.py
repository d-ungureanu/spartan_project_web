from flask import Flask, redirect, url_for, render_template, request
from spartan import Spartan

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_spartan():
    if request.method == "POST":
        spartan_id = request.form["spartan_id"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        birthday = request.form["birthday"]
        birthmonth = request.form["birthmonth"]
        birthyear = request.form["birthyear"]
        course = request.form["course"]
        stream = request.form["stream"]
        spartan = Spartan(spartan_id, firstname, lastname, birthday, birthmonth, birthyear, course, stream)
        return spartan
    else:
        return render_template("add_details.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


@app.route("/spartan/<spartan_id>", methods=["GET"])
def spartan_getter(spartan_id):
    return f"You are asking about spartan with ID: {spartan_id}"


@app.route("/spartan/remove", methods=["POST"])
def remove_spartan():
    id_var = request.args.get("id")
    return f"Remove spartan with ID: {id_var}."


@app.route("/spartan", methods=["GET"])
def list_spartans():
    return "Spartans list page."


if __name__ == '__main__':
    app.run(debug=True)
