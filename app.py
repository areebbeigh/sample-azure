from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! - Areeb Beigh 2018BITE029"
