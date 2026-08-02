from flask import Flask # we are importing Flask from flask 

app = Flask(__name__)  # we are making an object of the flask that represent our website

@app.route("/") #this is our home page
def home(): # we define a function that is connected to our home page
    return "Hello Everyone ! This is my first flask app." # we return a string that is visible in our home page

if __name__ == "__main__":
    app.run(debug=True)