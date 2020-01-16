from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

from const import (
    title,
    url_regex,
    invalid_url_msg,
)

app = Flask(__name__)


def valid_url(url: str) -> bool:
    if url_regex.search(url):
        return True
    else:
        return False


@app.route('/')
def index():
    return render_template("index.html", title=title)


@app.route("/prediction", methods=["POST"])
def prediction_hatebu():
    url = request.form["url"]
    if not valid_url(url):
        return render_template("index.html",
                               title=title,
                               err_msg=invalid_url_msg)
    return render_template("index.html", title=title, url=url)


if __name__ == "__main__":
    app.run(port=18000, host="0.0.0.0", debug=True)
