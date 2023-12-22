from django.db import models
from constant.mixin import DateTimeMixin
from user.models import User
from page.models import Page


class Post(DateTimeMixin, models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["author", "page", "content"]


class Like(DateTimeMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
        ordering = ["user", "post", "is_liked"]

