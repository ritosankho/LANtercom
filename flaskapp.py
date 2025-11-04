from flask import Flask, redirect, url_for, request, render_template
from chat import start_chat_server

users = {
    "admin":"admin"
}

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            print(username)
            print(password)
            if username in users and users[username] == password:
                return render_template("chatRoom.html")
            else:
                return render_template("loginFailure.html")
            
    
    return render_template("login.html")

'''@app.route("/chatroom" , methods = ["GET", "POST"])
def chatroom():
    if username in users and users[username] == password:
        return render_template("loginSuccess.html")
    else:
        return render_template("loginFailure.html")'''
   


