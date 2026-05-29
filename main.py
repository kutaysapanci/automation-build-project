from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Merhaba Flask!"

@app.route("/about")
def about():
    return "Hakkımızda sayfası"

if __name__ == "__main__":
    app.run(debug=True)