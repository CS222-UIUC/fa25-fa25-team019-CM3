import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

print(f"Testing with: {EMAIL_ADDRESS}")
print(f"Password length: {len(EMAIL_PASSWORD)}")

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    print(" SUCCESS! Credentials work!")
    server.quit()
except Exception as e:
    print(f" FAILED: {e}")