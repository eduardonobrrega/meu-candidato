from cs50 import SQL
from flask import Flask, render_template, request
from flask_session import Session
# Configure o app
app = Flask(__name__)

# Configure a sessão
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite:///my_candidate.db")

@app.route("/")
def index():
    # user = db.execute("SELECT * FROM users")
    # print(user[0])
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    
    # POST
    if request.method == "POST":
        return render_template("login.html")
    return render_template("register.html")
