from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

app = Flask(__name__)
TITLE = "velvet"


@app.route('/')
def index():
    return render_template("index.html", title=TITLE)


@app.route("/prediction", methods=["GET", "POST"])
def prediction_hatebu():
    if request.method == "POST":
        url = request.form["url"]
        return render_template("index.html", title=TITLE, url=url)
    else:
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(port=18000, host="0.0.0.0", debug=True)
