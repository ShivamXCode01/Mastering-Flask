from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecret"  # user session securely

# homepage Login Here
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        Username = request.form["username"]
        Password = request.form["password"]

        if Username == "admin" and Password == "123":
            session["user"] = Username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid Details. Try Again", mimetype="text/plain")

    return '''
    <h2>Login Page</h2>

    <form method="POST">
        Username:
        <input type="text" name="username"><br><br>

        Password:
        <input type="password" name="password"><br><br>

        <input type="submit" value="Login">
    </form>
    '''

# Welcome page after login
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome, {session["user"]}!</h2>
        <a href="{url_for('logout')}">Logout</a>
        '''
    return redirect(url_for("login"))

# logout route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

