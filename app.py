from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index_rt():
    return render_template("index.html")

@app.route("/editor")
def editor_rt():
    return render_template("editor.html")