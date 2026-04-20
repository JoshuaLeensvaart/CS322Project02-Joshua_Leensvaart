from flask import Flask, render_template

app = Flask(__name__)
pangolin_logs = [
    {"id": 1, "location": "Congo Basin", "weight": 4.5, "date": "2026-04-20"}
]
@app.route("/")
def index():
    # We pass the entire list to the frontend (Pattern from PDF Page 3)
    return render_template('index.html', logs=pangolin_logs)
def home():
    return '''
        <h1>Welcome to the edge of Pangolins</h1>
        <p>Click below to see something cool:(Spoiler alert: its pangolins)</p>
        <a href="/lab09">See Pangolins!</a>
    '''

@app.route("/lab09")
def pangolins():
    return render_template("lab09.html")