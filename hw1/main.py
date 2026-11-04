from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    count, text = None, ""
    if request.method == "POST":
        text = request.form["text"]
        count = sum(1 for char in text if char.lower() in "aeiou")
    return render_template("index.html", count=count, text=text)

if __name__ == "__main__":
    app.run(debug=True)
