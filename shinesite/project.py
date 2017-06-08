from flask import Flask
from dbclass import dbClass

app = Flask(__name__)


@app.route('/')
def onboarding():
    return 'Hello World!'

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("error.html", error=error)

if __name__ == '__main__':
    app.run(debug=True)
