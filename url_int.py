from flask import Flask
app = Flask(__name__)

@app.route("/add/<int:first>/<int:second>")
def hello(first, second):
    return str(first+second)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
