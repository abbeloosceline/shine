from flask import Flask, render_template, abort
from dbclass import DbClass

app = Flask(__name__)


@app.route('/')
def onboarding():
    return render_template("onboarding.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/alarms')
def alarms():
    return render_template("alarms.html")

@app.route('/alarms/add')
def addalarm():
    return render_template("addalarm.html")

@app.route('/nights')
def nights():
    return render_template("nights.html")

@app.route('/nights/add')
def addnight():
    return render_template("addalarm.html")

@app.route('/sleepcharts')
def sleepcharts():
    return render_template("sleepcharts.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")


@app.errorhandler(404)
def pagenotfound(error):
    return render_template("error.html", error=error)


if __name__ == '__main__':
    app.run(debug=True)
