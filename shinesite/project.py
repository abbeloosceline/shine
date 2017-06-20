import calendar
import datetime
import time

from flask import Flask, render_template, request, Markup

from shinesite.dbclass import DbClass

time.sleep(15)

app = Flask(__name__)
db = DbClass()

def printresults():
    print

@app.route('/')
def onboarding():
    return render_template("onboarding.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/home')
def home():
    result = db.getAlarmToday()
    alarm = result[0]
    wakeup = result[1]
    return render_template("home.html", alarm=alarm, wakeup=wakeup)


@app.route('/alarms')
def alarms():
    result = db.getAlarmToday()
    alarm = result[0]
    wakeup = result[1]
    month = "<h2>" + datetime.datetime.now().strftime("%B") + "</h2>"
    html = "<table>"
    kalender = ""
    for week in calendar.monthcalendar(2017, 3):
        kalender += "<tr>"
        for day in week:
            if day == datetime.date.today().day:
                kalender += "<td style='background-color: #e6aa00; color:white;'>"
            elif day == 0:
                kalender += "<td style='background-color: #FcFbFa;'>"
            else:
                kalender += "<td>"
            if day == 0:
                kalender += " "
            else:
                kalender += str(day)
            kalender += "</td>"
        kalender += "</tr>"
    html += kalender
    html += "</table>"
    return render_template("alarms.html", alarm=alarm, wakeup=wakeup, month=month, kalender=Markup(html))


@app.route('/alarms/add', methods=['GET', 'POST'])
def addalarm():
    musiclist = db.getSounds()
    if request.method == 'POST':
        if request.form['sunrise']: sunrise = 1
        else: sunrise = 0
        if request.form['snooze']: snooze = 1
        else: snooze = 0
        if request.form['name']: name = request.form['name']
        else: name = 0
        if request.form['date']: date = request.form['date']
        else: date = 0
        if request.form['monday']: mon = 1
        else: mon = 0
        if request.form['tuesday']: tue = 1
        else: tue = 0
        if request.form['wednesday']: wen = 1
        else: wen = 0
        if request.form['thursday']: thu = 1
        else: thu = 0
        if request.form['friday']: fri = 1
        else: fri = 0
        if request.form['saturday']: sat = 1
        else: sat = 0
        if request.form['sunday']: sun = 1
        else: sun = 0
        print(sunrise, snooze, name, date, mon, tue, wen, thu, fri, sat, sun)
    return render_template("addalarm.html", musiclist=musiclist)


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
    app.run(host="0.0.0.0",
            debug=True)