from django.db import models
from constant.mixin import DateTimeMixin
from user.models import User
from page.models import Page


class Post(DateTimeMixin, models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(DateTimeMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=True)

