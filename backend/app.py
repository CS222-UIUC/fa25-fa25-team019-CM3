from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
      <h1>Home</h1>
      <p><a href="{url_for('email_templates')}">Email Templates</a></p>
    """

@app.route("/email-templates")
def email_templates():
    return render_template("email_templates.html")

if __name__ == "__main__":
    app.run(debug=True)
