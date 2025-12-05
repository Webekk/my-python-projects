import smtplib, ssl
from dotenv import load_dotenv
from email.message import EmailMessage
import os
load_dotenv()

smtp_server = "smtp.gmail.com"
smtp_port = 465
sender_email = os.getenv("GMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
password = os.getenv("SMTP_PASSWORD")
msg = EmailMessage() #Create an instance of EmailMessage
msg["Subject"] = "Subject"
msg["From"] = sender_email
msg["To"] = receiver_email

msg.set_content("""Message sent by using python""")
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
    server.login(sender_email, password)
    server.send_message(msg)
print(f"Email sent to {receiver_email}")
