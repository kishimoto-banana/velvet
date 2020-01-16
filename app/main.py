import yaml
import requests
from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

from const import (
    config_path,
    title,
    hatebu_prediction_path,
    url_regex,
    invalid_url_msg,
)

with open(config_path, "r", encoding="utf-8") as f:
    config = yaml.load(stream=f, Loader=yaml.SafeLoader)

app = Flask(__name__)


def valid_url(url: str) -> bool:
    if url_regex.search(url):
        return True
    else:
        return False


def get_hatebu(url: str) -> dict:
    address = config["velvet-api"]["address"]
    request_url = f"http://{address}{hatebu_prediction_path}?url={url}"
    res = requests.get(request_url)
    hatebu_info = res.json()

    return hatebu_info


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
    hatebu_info = get_hatebu(url)

    return render_template("index.html",
                           title=title,
                           is_hatebu=hatebu_info["is_hatebu"],
                           hatebu_num=hatebu_info["hatebu_num"])


if __name__ == "__main__":
    app.run(port=18000, host="0.0.0.0", debug=True)
