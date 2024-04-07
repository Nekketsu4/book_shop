from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):

    """
    Расширяемм модель User добавив свойство send_messages,
    для возможности получения уведомлений
    """

    send_messages = models.BooleanField(
        'Присылать уведомления о поступлении новых книг?',
        default=True
    )

    class Meta(AbstractUser.Meta):
        pass


class Book(models.Model):

    name = models.CharField('Название', max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class UserBook(models.Model):

    """
    Промежуточная модель для AdvUser и Book
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_book',
        on_delete=models.PROTECT
    )

    book = models.ForeignKey(
        Book,
        related_name='user_book',
        on_delete=models.PROTECT
    )

    favorites = models.BooleanField(
        'Добавить в избранное?',
        default=False
    )

    was_read = models.BooleanField(
        'Прочитано?',
        default=False
    )


class Comment(models.Model):

    content = models.TextField('Комментарий', max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, )

    book = models.ForeignKey(
        Book,
        related_name='comments',
        on_delete=models.PROTECT
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
