import os
import smtplib
from email.message import EmailMessage

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("APP_PASSWORD")

def send_application(job, cover_letter):
    msg = EmailMessage()
    msg["Subject"] = f"Application for {job.get('position')}"
    msg["From"] = EMAIL
    msg["To"] = job.get("email")

    msg.set_content(cover_letter)

    with open("resume.pdf", "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename="Resume.pdf"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)