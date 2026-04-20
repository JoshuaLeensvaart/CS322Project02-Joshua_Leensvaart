from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <h1>Welcome to the edge of Pangolins</h1>
        <p>Click below to see something cool:(Spoiler alert: its pangolins)</p>
        <a href="/lab09">See Pangolins!</a>
    '''

@app.route("/lab09")
def pangolins():
    return render_template("lab09.html")
