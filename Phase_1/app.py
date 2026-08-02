# HTTP Methods 
from flask import Flask,request,redirect,url_for

# By default flask uses GET method through that we can only see the data 
# with the help of POST method we can send some data that can be processed 

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("submit" ,msg="You are rediredcted to submit page."))

@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method == "POST":
        return "You sent some data.."
    else:
        return "You just see the data.."

if __name__ == "__main__":
    app.run(debug=True)