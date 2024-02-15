import ssl
import smtplib
import os

from email.message import EmailMessage


def deliver_email(email_receiver, otp):
    email_sender = os.getenv('EMAIL_SENDER')
    email_password = os.getenv('EMAIL_PASSWORD')

    subject = 'Your OTP from Better App!'

    body = f"""
    Hi User,
    
    Greetings from Better App!
    
    Here is your OTP: {otp}. Please do not share this with anyone.
    The OTP is valid for 20 minutes.
    
    Best Regards,
    Team Better
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
