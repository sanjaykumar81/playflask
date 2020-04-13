from flask import Flask

app = Flask('__name__')


@app.route("/")
def hello():
    return "Welcome to flask"

"""
Example for working with the path param
"""
@app.route("/hello/<name>")
def hello_path_param(name):
    return f"welcome '{name}' to flask world"

if __name__ == "__main__":
    app.run()
