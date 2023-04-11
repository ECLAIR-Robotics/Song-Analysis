from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/Mehul")
def mehul():
    return "Hello, Mehul"
    
if __name__ == "__main__":
    app.run(debug=True)