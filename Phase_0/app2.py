from flask import Flask

app2 = Flask(__name__)

@app2.route("/")
def home():
    return "We are in the home page "

@app2.route("/about")
def about ():
    return "We are in the about page"

@app2.route("/contact")
def contact():
    return "We are in the contact page"

if __name__ == "__main__":
    app2.run(debug=True)

# we can move to the different pages just change in the url like http://127.0.0.1:5000/about , contact etc