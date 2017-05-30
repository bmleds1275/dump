from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('hello.html')


@app.route("/staff")
def yup():
    return "Something about dogs"

@app.route("/bootstrap")
def boot():
    return render_template('bootstrap.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
