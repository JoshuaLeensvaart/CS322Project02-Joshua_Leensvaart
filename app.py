import re
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
pangolin_logs = [
    {"id": 1, "location": "Congo Basin", "weight": 4.5, "date": "2026-04-20"}
]
@app.route("/")
def index():
    return render_template('index.html', logs=pangolin_logs)


def add_entry():
    loc = request.form.get("loc").strip()
    wgt = request.form.get("wgt").strip()
    dt = request.form.get("dt").strip()

    if not re.match(r"^[a-zA-Z\s]{3,30}$", loc):
        flash("Location must be 3-30 letters only.")
        return redirect(url_for('index'))

    try:
        wgt_float = float(wgt)
        if not (1.0 <= wgt_float <= 45.0):
            flash("Weight must be between 1kg and 45kg.")
            return redirect(url_for('index'))
    except ValueError:
        flash("Weight must be a decimal number.")
        return redirect(url_for('index'))

    new_id = max([x['id'] for x in pangolin_logs], default=0) + 1
    pangolin_logs.append({"id": new_id, "location": loc, "weight": wgt_float, "date": dt})

    return redirect(url_for('index'))
def home():
    return '''
        <h1>Welcome to the edge of Pangolins</h1>
        <p>Click below to see something cool:(Spoiler alert: its pangolins)</p>
        <a href="/lab09">See Pangolins!</a>
    '''

@app.route("/lab09")
def pangolins():
    return render_template("lab09.html")