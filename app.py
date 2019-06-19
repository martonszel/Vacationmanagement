from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route("/hello/")
@app.route("/hello/<name>")
def vacationmanagement(name=None):
    return render_template(
        "Vacationmanagement.html",
        name=name,
    )
@app.route("/api/data/")
def get_data():
    return app.send_static_file("data.json")
