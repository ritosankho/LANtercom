from flask import Flask, redirect, url_for, request, render_template
#from chat import start_chat_server          #importing the function from chat.py
from userAuth import users    #Importing users dictionary

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            print(username)           #Logs which user has tried connecting. 
            print(password)
            if username in users and users[username] == password:         #Check if the creds match and go from there. 
                return render_template("chatRoom.html")
            else:
                return render_template("loginFailure.html")
            
    
    return render_template("login.html")




