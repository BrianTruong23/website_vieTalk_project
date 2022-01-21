
from flask import Flask, render_template, redirect, url_for, flash,g, abort
from flask_bootstrap import Bootstrap


app = Flask(__name__)

Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
