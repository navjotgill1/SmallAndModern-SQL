from flask import Flask, render_template, request, flash

import main


app = Flask(__name__)


#creates the landing page for the web abb
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def insert():
    text = request.form['name']
    main.add(text)
    return None


if __name__ == "__main__":
    app.run()