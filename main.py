from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from flask_login import login_manager, login_required, logout_user
from flask_session import Session
from random import randint

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = "YOU*T*O8346grf9"
sess = Session()

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        req = request.form

        username = str(req.get("username"))
        password = str(req.get("password"))
        print(type(username))

        if username != "admin":
            print("Username not found username: " + str(username))
            return redirect(request.url)
        else:

	        if not password == str("\"or\"\"=\""):
	            print("Incorrect password" + str(password))
	            print("password" + """ "or""=" """)
	            return redirect(request.url)
	        else:
	            session["USERNAME"] = randint(100000, 999999)
	            print(str(session["USERNAME"]) + "logged in, info: " + str(request.environ.get('HTTP_X_REAL_IP', request.remote_addr)))
	            return redirect(url_for("admin"))

    return render_template("index.html")

@app.route("/admin")
def admin():

    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")

        return render_template("admin.html")
    else:
        print("No username found in session")
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)