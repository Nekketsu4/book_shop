from django.dispatch import receiver
from django.db.models.signals import post_save
from books.services import send_notification

from books.models import Book


@receiver(post_save, sender=Book)
def post_save_send_notification(**kwargs):
    send_notification()
    print("Уведомление отправлено!")
