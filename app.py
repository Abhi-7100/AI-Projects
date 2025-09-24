from flask import Flask, render_template, request
import openai, os

app = Flask(__name__)

# Use environment variable for security
openai.api_key = os.environ.get("OPENAI_API_KEY", "your openai API key")

def ai_tutor(question, subject="math"):
    """AI Tutor function that answers questions step by step."""
    prompt = f"You are an AI Tutor specialized in {subject}. " \
             f"Explain the following question step by step:\n\n{question}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful and patient AI Tutor."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        temperature=0.5
    )
    return response["choices"][0]["message"]["content"]

@app.route("/", methods=["GET", "POST"])
def home():
    answer = "Bot: Hello! How can I assist you?"
    user_message = "User: Hello!"
    if request.method == "POST":
        user_message = "User: " + request.form["question"]
        answer = "Bot: " + ai_tutor(request.form["question"])
    return render_template("index.html", answer=answer, user_message=user_message)

if __name__ == "__main__":
    app.run(debug=True)
