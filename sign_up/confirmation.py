from flask_mail import Mail, Message
from Project.settings import mail

def confirmation_email(user_email):
    message = Message(
        subject="Подтверждение регистрации",
        # sender="gmail@gmail.com", почта отправителя 
        recipients=[user_email]
    )
    message.body = "Спасибо за регистрацию! Подтвердите свою почту, перейдя по ссылке: https://your-domain.com/confirm?email=" + user_email
    mail.send(message)

