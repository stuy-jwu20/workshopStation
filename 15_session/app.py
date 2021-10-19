# Team The Best Laptop - Jonathan W. [Loki] , Alif A. [The Eagle in the Sand], Kevin C. [Pipi] | Period 2
# SoftDev
# K15 - Sessions Greetings/More form handling in HTML in flask app/We worked on creating a flask app that uses session capabilities to allow a user to login and logout.
# 2021-10-18

from flask import Flask             # facilitate flask webserving
from flask import render_template   # facilitate jinja templating
from flask import request           # facilitate form submission
app = Flask(__name__)


@app.route("/")  # , methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.headers ***")
    print(request.headers)
    landingText = "Enter your username below to proceed."
    return render_template('login.html', message = landingText)


@app.route("/auth")
def response():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.headers ***")
    print(request.headers)
    user0 = 'kevinjonleafy'
    passw0 = 'dellthebestlaptop15'
    loadText = ""
    user = ""
    passw = ""
    if request.method == 'GET':
        user = request.args['username']
        passw = request.args['password']
    elif request.method == 'POST':
        user = request.form['username']
        passw = request.form['password']
    if user0 != user and passw0 != passw:
        loadText = "Could not log in. User and password wrong."
        return render_template("login.html", message = loadText)
    elif user0 != user and passw0 == passw:
        loadText = "Could not log in. User is wrong."
        return render_template("login.html", message = loadText)
    elif user0 == user and passw0 != passw:
        loadText = "Could not log in. Password is wrong."
        return render_template("login.html", message = loadText)
    else:
        loadText = "Click the button below to logout."
        return render_template("response.html", username=user, password=passw, request_method = request.method, message = loadText)

@app.route("/logout")
def logoutSession():
    landingText = "You've logged out. Enter your username below to proceed. "
    return render_template("login.html", message = landingText)

if __name__ == "__main__":
    app.debug = True
    app.run()
