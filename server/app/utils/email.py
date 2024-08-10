from flask_mail import Message
from ..configs import Config

def send_email(to, subject, content):
    from app import mail
    msg = Message(
        subject=subject,
        recipients=[to],
        sender=Config.MAIL_USERNAME,
    )
    msg.body = content
    mail.send(msg)