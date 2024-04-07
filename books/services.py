from django.core.mail import send_mail
from server.settings import EMAIL_HOST


def send_notification():
    from books.models import AdvUser

    """
    отправка уведомления
    """

    mails = AdvUser.objects.all()

    send_mail(
        subject='Новые книги',
        message='В наш магазин поступили новинки',
        from_email=EMAIL_HOST,
        recipient_list=[mail.email for mail in mails]
    )
