from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def devops():
    return render_template("base.html")