from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/goodbye")
def goodbye_world():
    return "<p>Goodbye, World!</p>"

@app.route("/ryan")
def ryans_endpoint():
    return "<p>Hello, Ryan!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)