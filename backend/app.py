import os
import requests # run pip install requests inside ur venv
from flask import Flask, render_template, url_for, requestpp = Flask(__name__)

#used AI to help with the generate_email function
#now the result that I get must be the result of generative ai thing and can we use gemini because there is no paywall

#NEXT STEP: get the API key
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

def generate_email(prompt, tone):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini‑2.5‑flash:generateContent"
    headers = {
        "x-goog-api-key": GEMINI_KEY, # add the key here
        "Content-Type": "application/json"
    }
    body = {
        "contents": [
          {
            "parts": [
              {"text": f"Write a {tone.lower()} professional email about: {prompt}"}
            ]
          }
        ]
    }
    resp = requests.post(url, json=body, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]

# DO NOT CHANGE the routing to home.html please
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        prompt = request.form.get("prompt")
        tone = request.form.get("tone")
        result = generate_email(prompt, tone)
    return render_template("home.html", result=result)

@app.route("/email-templates")
def email_templates():
    return render_template("email_templates.html")

if __name__ == "__main__":
    app.run(debug=True)

