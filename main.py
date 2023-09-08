from flask import Flask, render_template
from app import deep
application = Flask(__name__)


@application.route("/")
def index():
    deep()
    return render_template('index.html')


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug=True)
