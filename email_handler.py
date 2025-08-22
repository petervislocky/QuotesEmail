import smtplib
import os
from pathlib import Path

from email.message import EmailMessage
from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent

load_dotenv(BASE_DIR / ".env")
from_email = os.getenv('FROM_EMAIL')
to_email = os.getenv("TO_EMAIL")

def form_email(quote: str, author: str) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = "Motivational quote of the day!"
    message["From"] = from_email
    message["To"] = to_email
    message.set_content(f"{quote}\n- {author}")
    return message

def send_email(message: EmailMessage) -> None:
    password = os.getenv("PASSWORD")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        if password is not None and from_email is not None:
            server.login(from_email, password)
        else:
            raise FileNotFoundError(".env file is missing or not containing item PASSWORD or item FROM_EMAIL")
        server.send_message(message)