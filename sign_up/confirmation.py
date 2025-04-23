from flask_mail import Message
from Project.settings import mail  

def confirmation_email(user_email):
    print(f"Отправка письма на {user_email}")
    message = Message(
        subject="Подтверждение регистрации",
        sender="egor115819@gmail.com", 
        recipients=[user_email]
    )
    
    confirmation_link = f"http://127.0.0.1:5000/confirmation?user_email={user_email}"
    message.body = f"Спасибо за регистрацию! Подтвердите свою почту по ссылке: {confirmation_link}"
    mail.send(message)
