import smtplib, ssl
import os

HOST = "smtp.gmail.com"
MY_EMAIL = "kyligalway@gmail.com"
PORT = 465
PASSWORD = os.getenv("PASSWORD")
CONTEXT = ssl.create_default_context()


def email_news(message, subject):
    """
    This function receives a message, subject, and username, and sends the
    message to my email address with the correct subject line and origin name.
    """

    message = f"""\
Subject: {subject}
    
News articles of note: 
    
{message}
"""
    message.encode("utf-8")
    with smtplib.SMTP_SSL(HOST, PORT, context=CONTEXT) as server:
        server.login(MY_EMAIL, PASSWORD)
        server.sendmail(MY_EMAIL, MY_EMAIL, message)
