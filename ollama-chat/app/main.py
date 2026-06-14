from flask import Flask, Response, render_template, request, session
import requests
import os
import json
from flask_session import Session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for Flask sessions
app.config["SESSION_TYPE"] = "filesystem"  # store sessions locally
Session(app)

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/stream", methods=["POST"])
def stream_chat():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return Response("No message provided", status=400)

    # Load or initialize conversation
    if "conversation" not in session:
        session["conversation"] = []

    # Append user message
    session["conversation"].append({"role": "user", "content": user_message})
    session.modified = True

    def generate():
        with requests.post(
            f"{OLLAMA_HOST}/api/chat",
            json={
                "model": "llama3",
                "messages": session["conversation"],
                "stream": True,
            },
            stream=True,
        ) as r:
            bot_reply = ""
            for line in r.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode("utf-8"))
                        token = data.get("message", {}).get("content", "")
                        if token:
                            bot_reply += token
                            yield token
                    except Exception as e:
                        yield f"[Error: {e}]"

            # Save assistant’s full reply to session
            session["conversation"].append({"role": "assistant", "content": bot_reply})
            session.modified = True

    return Response(generate(), mimetype="text/plain")


@app.route("/reset", methods=["POST"])
def reset_conversation():
    """Clear the current chat session."""
    session.pop("conversation", None)
    return {"status": "ok", "message": "Conversation reset."}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
