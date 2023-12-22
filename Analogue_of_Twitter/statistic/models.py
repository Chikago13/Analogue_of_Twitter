from django.db import models
from constant.mixin import DateTimeMixin
from page.models import Page
from user.models import User


class PageStatistic(DateTimeMixin, models.Model):
    page = models.OneToOneField(Page, on_delete=models.CASCADE, related_name='statistics')
    post_count = models.PositiveIntegerField(default=0, verbose_name="Количество постов")
    subscriber_count = models.PositiveIntegerField(default=0, verbose_name="Количество подписчиков")
    like_count = models.PositiveIntegerField(default=0, verbose_name="Количество лайков")

    class Meta:
        verbose_name = "Статистика страницы"
        verbose_name_plural = "Статистика страниц"
        ordering = ["page", "post_count", "subscriber_count"]

class Notification(DateTimeMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    subject = models.CharField( max_length=255, verbose_name="Тема уведомления")
    message = models.TextField(verbose_name="Сообщение")

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомлении"
        ordering = ["user", "subject"]