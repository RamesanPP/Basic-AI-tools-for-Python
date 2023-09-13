from flask import Flask, request, render_template
from openAI_response_assistant import generate_summary
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  # Enable CORS for your Flask app

@app.route("/", methods=["GET", "POST"])
def home():
    user_input = ""
    response = ""

    if request.method == "POST":
        user_input = request.form["user_input"]
        # Call the required function from the assistant
        response = generate_summary(user_input)

    return render_template("index.html", user_input=user_input, response=response)

## Provide necessary routes for API Calls

# # Route for Techno/Salesy/Factual Response Types
# @app.route("/api/generate/<response_type>", methods=["POST"])
# def generate_response(response_type):
#     user_input = request.get_json().get("inputText")
#     if response_type == "techno":
#         response = generate_response_techno(user_input)
#     elif response_type == "salesy":
#         response = generate_response_salesy(user_input)
#     elif response_type == "factual":
#         response = generate_response_factual(user_input)
#     else:
#         response = "Invalid response type"

#     return jsonify({"response": response})

# # Route for generating summaries
# @app.route("/api/summarize", methods=["POST"])
# def summarize():
#     data = request.get_json()
#     input_text = data.get("inputText")
#     summary = generate_summary(input_text)
#     return jsonify({"summary": summary})

# # Route for generating elaborations
# @app.route("/api/elaborate", methods=["POST"])
# def elaborate():
#     data = request.get_json()
#     input_text = data.get("inputText")
#     elaboration = generate_elaboration(input_text)
#     return jsonify({"elaboration": elaboration})

# # Route for generating bullet lists
# @app.route("/api/bullet-list", methods=["POST"])
# def bullet_list():
#     data = request.get_json()
#     input_text = data.get("inputText")
#     bullet_list = generate_bullet_list(input_text)
#     return jsonify({"bulletList": bullet_list})

# # Route for content response
# @app.route("/api/content_repo", methods=["POST"])
# def content_repo():
#     data = request.get_json()
#     input_text = data.get("inputText")
#     content_response = generate_content_response(input_text)
#     return jsonify({"contentResponse": content_response})



if __name__ == "__main__":
    app.run(debug=True)

