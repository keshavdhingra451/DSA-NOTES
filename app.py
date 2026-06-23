from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to DSA Notes</h1>"

@app.route("/arrays")
def arrays():
    return render_template("arrays.html")

@app.route("/linkedlist")
def linkedlist():
    return render_template("linkedlist.html")

if __name__ == "__main__":
    app.run(debug=True)