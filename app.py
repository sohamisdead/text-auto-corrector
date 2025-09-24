from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    corrected_text = None
    input_text = None

    if request.method == "POST":
        input_text = request.form.get("text")
        if input_text.strip():
            blob = TextBlob(input_text)
            corrected_text = str(blob.correct())

    return render_template("index.html", input_text=input_text, corrected_text=corrected_text)

if __name__ == "__main__":
    app.run(debug=True)