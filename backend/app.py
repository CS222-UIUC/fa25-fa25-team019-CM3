from flask import Flask, render_template, request, url_for
import openai # currently we are trying to use openai (might change later if it doesn't work)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    email_output = None
    if request.method == "POST":
        user_prompt = request.form.get("prompt")
        tone = request.form.get("tone", "friendly")
        if user_prompt:
            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": f"You are an email assistant that writes {tone} emails."},
                    {"role": "user", "content": user_prompt}
                ]
            )
            email_output = response["choices"][0]["message"]["content"]
    return render_template("home.html", result=email_output)

@app.route("/email-templates")
def email_templates():
    return render_template("email_templates.html")

if __name__ == "__main__":
    app.run(debug=True)

