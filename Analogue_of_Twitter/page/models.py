from django.db import models
from constant.mixin import DateTimeMixin
from user.models import User


class Tag(DateTimeMixin, models.Model):
    name = models.CharField(max_length=200, verbose_name="Название тега")


class Page(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pages')
    title = models.CharField(max_length=200)
    uuid = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='pages')
    is_private = models.BooleanField(default=False)
    subscribers = models.ManyToManyField(User, related_name='subscribed_pages', blank=True)


class Subscription(DateTimeMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='subscriptions')
    is_confirmed = models.BooleanField(default=False)


class BlockedPage(DateTimeMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked_pages')
    page = models.ForeignKey(Page, on_delete=models.CASCADE)


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    is_approved = models.BooleanField(default=False, verbose_name="Одобрено")