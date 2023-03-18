from flask import Flask

app = Flask(__name__, )

@app.route("/")
def hello_world():
    return "Hello World. This is 石泽楷's html."

app.debug = True

app.run(host="0.0.0.0",port=70)


