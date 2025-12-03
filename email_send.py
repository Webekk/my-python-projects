import os

import requests
import smtplib, ssl

from dotenv import load_dotenv

# Replace with your email provider's SMTP server and your credentials
smtp_server = "smtp.gmail.com"
smtp_port = 587 # Or the appropriate port for your provider
sender_email = os.getenv("GMAIL")
sender_password = os.getenv("SMTP_PASSWORD")

receiver_email = os.getenv("GMAIL")
message = f"""\
Subject: Hello from Python

This is a test email sent from Python."""

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls() # Secure the connection
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
finally:
    server.quit()





