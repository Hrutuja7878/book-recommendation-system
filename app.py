from flask import Flask, render_template, request
from book_recommendation import recommend

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/explore", methods=["GET", "POST"])
def explore():
    recommendations = []

    if request.method == "POST":
        book = request.form.get("book", "")
        mood = request.form.get("mood", "")

        recommendations = recommend(book, mood)

    return render_template(
        "explore.html",
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)