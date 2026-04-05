from flask import render_template, url_for
from myfiles import app


@app.route("/")
def homepage():
    return render_template("defaultpage.html")

@app.route("/login")
def loginpage():
    return render_template("loginpage.html")

@app.route("/signin")
def signinpage():
    return render_template("signinpage.html")

@app.route("/profile/<user>")
def user_profile(user):
    return render_template("userprofile.html",user=user)