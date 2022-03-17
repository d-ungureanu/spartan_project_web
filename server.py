from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Welcome to app's homepage!"


@app.route("/spartan/add", methods=["POST"])
def add_spartan():
    return "ADD spartan page!"


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
