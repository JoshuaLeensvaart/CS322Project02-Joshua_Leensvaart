import datetime
import re
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
pangolin_logs = [
    {"id": 1, "location": "Congo Basin", "weight": 4.5, "date": "2026-04-20"}
]
@app.route("/")
def index():
    return render_template('index.html', logs=pangolin_logs)

@app.route('/add', methods=['POST'])
def add_entry():
    loc = request.form.get("loc").strip()
    wgt = request.form.get("wgt").strip()
    dt = request.form.get("dt").strip()

    if not re.match(r"^[a-zA-Z\s]{3,30}$", loc):
        flash("Location must be 3-30 letters only.")
        return redirect(url_for('index'))
    if not dt:
        flash("Date is required.")
        return redirect(url_for('index'))
    try:
        input_date = datetime.datetime.strptime(dt, '%Y-%m-%d').date()
        today = datetime.date.today()

        if input_date > today:
            flash("Date Error: Cannot log a future sighting.")
            return redirect(url_for('index'))
    except ValueError:
        flash("Invalid date format.")
        return redirect(url_for('index'))
    try:
        wgt_float = float(wgt)
        if not (0.1 <= wgt_float <= 45.0):
            flash("Weight must be between 0.1kg and 45kg.")
            return redirect(url_for('index'))
    except ValueError:
        flash("Weight must be a decimal number.")
        return redirect(url_for('index'))

    new_id = max([x['id'] for x in pangolin_logs], default=0) + 1
    pangolin_logs.append({"id": new_id, "location": loc, "weight": wgt_float, "date": dt})

    return redirect(url_for('index'))
@app.route('/delete/<int:item_id>')
def delete_entry(item_id):
    global pangolin_logs
    pangolin_logs = [item for item in pangolin_logs if item['id'] != item_id]
    return redirect(url_for('index'))
app.run()
