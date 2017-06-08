from flask import Flask, render_template, abort
from dbclass import DbClass

app = Flask(__name__)


@app.route('/')
def onboarding():
    return render_template("onboarding.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.errorhandler(404)
def pagenotfound(error):
    return render_template("error.html", error=error)


if __name__ == '__main__':
    app.run(debug=True)
