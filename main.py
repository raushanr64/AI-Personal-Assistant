
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from anthropic import Anthropic

app = Flask(__name__)

load_dotenv()

api_key = os.getenv("CLAUDE_API_KEY")
MODEL = "claude-haiku-4-5-20251001"

if not api_key:
    raise ValueError("CLAUDE_API_KEY is missing. Check your .env file.")

client = Anthropic(api_key=api_key)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    try:
        question = request.form.get("question", "").strip()

        if not question:
            return jsonify({"error": "Please enter a question."}), 400

        response = client.messages.create(
            model=MODEL,
            max_tokens=512,
            system="Act like a helpful personal assistant.",
            messages=[
                {"role": "user", "content": question}
            ]
        )

        answer = response.content[0].text.strip()
        return jsonify({"response": answer}), 200

    except Exception as e:
        app.logger.exception("Error in /ask")
        return jsonify({"error": str(e)}), 500


@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        email_text = request.form.get("question", "").strip()

        if not email_text:
            return jsonify({"error": "Please paste an email to summarize."}), 400

        prompt = (
            "Summarize the following email in 2-3 sentences:\n\n"
            f"{email_text}"
        )

        response = client.messages.create(
            model=MODEL,
            max_tokens=512,
            system="Act like an expert email assistant.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        summary = response.content[0].text.strip()
        return jsonify({"response": summary}), 200

    except Exception as e:
        app.logger.exception("Error in /summarize")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
