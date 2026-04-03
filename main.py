from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)