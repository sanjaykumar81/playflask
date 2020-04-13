from flask import Flask, redirect, url_for, render_template

app = Flask('__name__')


@app.route("/")
def hello():
    return "Welcome to flask"


"""
Example - working with the path param
"""


@app.route("/hello/<name>")
def hello_path_param(name):
    return f"welcome '{name}' to flask world"


"""
Example - working with the path param with type
"""


@app.route("/hello/<int:number>")
def hello_path_param_type(number):
    return f"You have add {number} to flask world"


"""
Example - working with the '/' in the uri. '/' in end let you use the uri with and without '/'.
'/slash/' == '/slash' is True
"""


@app.route("/slash/")
def hello_slash():
    return f"welcome slash in path of flask world"


"""
Example - url_for() is use to dynamically redirect request to other functions  
"""


@app.route("/admin/<name>")
def hello_admin(name):
    return f"Welcome {name}. You are admin of flask world"


@app.route("/guest/<name>")
def hello_guest(name):
    if name == "sanjay":
        return redirect(url_for("hello_admin", name=name))
    else:
        return redirect(url_for("hello_user", user=name))


@app.route("/user/<user>")
def hello_user(user):
    return f"Welcome {user}. You are user of flask world"


"""
Example - Using  `render_template` to return a html page.
Also, using Jinga express to pass value from the route to html page.
"""


@app.route("/templates/<name>")
def flask_template(name):
    return render_template("index.html", user=name)


if __name__ == "__main__":
    app.run()
