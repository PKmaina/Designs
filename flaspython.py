from flask import Flask, render_template

app =Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.route('/list')
def list():
    return render_template("Yourlist.html")

if __name__ == "__main__":
    app.run(debug=True)