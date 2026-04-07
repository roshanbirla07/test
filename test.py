import smtplib
from email.mime.text import MIMEText
import os

def send_email(
    sender_email,
    app_password,
    receiver_email,
    subject,
    body
):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        # Gmail SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)

        print(f"✅ Email sent to {receiver_email}")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")

send_email(
    sender_email=os.getenv("EMAIL"),
    app_password=os.getenv("APP_PASSWORD"),
    receiver_email=os.getenv("RECEIVER"),
    subject="Automated Email 🚀",
    body="Sent via GitHub Actions"
)