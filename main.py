from flask import Flask, request, render_template

app = Flask(__name__)
print(__name__)


# http://127.0.0.1:5001/
@app.route("/", methods=["GET"])
def hello():
    return "<h1>Welcome to Python Flask Example</h1>"


# http://127.0.0.1:5001/hello
@app.route("/hello", methods=["GET"])
def greet():
    return "<h1>Hello World</h1>"


# http://127.0.0.1:5001/name
# This should return your name
@app.route("/name", methods=["GET"])
def name():
    print(request)
    return "<h1>Pritesh Patel</h1>"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=5001, debug=True)

