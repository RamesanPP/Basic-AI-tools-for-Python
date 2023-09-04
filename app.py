from flask import Flask, request, render_template
from summarization_assistant import generate_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    user_input = ""
    response = ""

    if request.method == "POST":
        user_input = request.form["user_input"]
        response = generate_response(user_input)

    return render_template("index.html", user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(debug=True)

