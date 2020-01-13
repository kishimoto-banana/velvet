from flask import Flask
from flask import render_template

app = Flask(__name__)
TITLE = "velvet"


@app.route('/')
def hello_world():
    return render_template('index.html', title=TITLE)


if __name__ == '__main__':
    app.run(port=18000, host='0.0.0.0')
