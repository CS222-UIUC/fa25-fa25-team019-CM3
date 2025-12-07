import os
import requests  # run pip install requests inside your venv
from flask import Flask, render_template, url_for, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

GEMINI_KEY = os.getenv("GEMINI_API_KEY")

def find_placeholders(text):
    return re.findall(r'\[([^\]]+)\]', text)

def generate_email(prompt, tone):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    headers = {
        "x-goog-api-key": GEMINI_KEY,  # Put your API key in the header
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

    try:
        resp = requests.post(url, json=body, headers=headers)
        resp.raise_for_status()
        data = resp.json()

        # DEBUG: print full API response
        print("API Response:", data)

        # Extract generated email text
        if "candidates" in data and len(data["candidates"]) > 0:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "Error: Unexpected API response. Check console for details."

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return f"Error: {e}"


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    placeholders = []
    email_html = None
    if request.method == "POST":
        prompt = request.form.get("prompt")
        tone = request.form.get("tone")
        result = generate_email(prompt, tone)
        placeholders = find_placeholders(result)

        # Replace placeholders with <input> tags
        email_html = result
        for ph in placeholders:
            email_html = email_html.replace(
                f'[{ph}]',
                f'<input type="text" name="{ph.replace(" ", "_")}" placeholder="{ph}">',
                1
            )

    return render_template("home.html", result=result, email_html=email_html)


@app.route("/email-templates")
def email_templates():
    return render_template("email_templates.html")


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")      # your email in environment variable
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")    # your Gmail app password

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    recipient = data.get('recipient')
    subject = data.get('subject', 'No Subject')
    body = data.get('body', '')

    if not recipient:
        return jsonify({"status": "error", "message": "Recipient is required"}), 400

    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        return jsonify({"status": "success", "message": "Email sent!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
