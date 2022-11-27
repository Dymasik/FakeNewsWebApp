from flask import Flask, request, render_template, redirect, url_for
from model.model import predict
from flask_ngrok import run_with_ngrok


app = Flask(__name__)
run_with_ngrok(app)

@app.route("/")
def index():
    return render_template(
        "index.html",
        article = "",
        is_calculated = False,
        score = 0
    )

@app.route('/', methods=['POST'])
def calculate():
    if request.form["sb-b"] == "calc":
        article = request.form["article"]
        score = predict(article)
        return render_template(
            "index.html",
            article = article,
            is_calculated = True,
            score = score
        )
    else:
        return redirect(url_for("index"))