from celery import shared_task
from django.core.mail import send_mail
from page.models import Subscription
from statistic.models import Notification
from django.db.models.signals import post_save
from django.dispatch import receiver
from post.models import Post
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@shared_task
def send_email_notifications(page_id):
    subscriptions = Subscription.objects.filter(page=page_id)
    page = subscriptions.first().page

    subject = f'New post on {page.name}'
    message = f'A new post has been published on {page.name}. Check it out!'
    from_email = 'noreply@example.com'
    recipient_list = [subscription.user.email for subscription in subscriptions]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)


#Создание задачи Celery для отправки уведомлений
@shared_task
def send_notification_email(notification_id):
    notification = Notification.objects.get(id=notification_id)
    user_email = notification.user.email
    message = f'Тема: {notification.subject}\n\n{notification.message}'
    send_mail(notification.subject, message, 'from@example.com', [user_email])


# Связывание уведомления с задачей Celery
@receiver(post_save, sender=Notification)
def send_notification_email_task(sender, instance, created, **kwargs):
    if created:
        send_notification_email.delay(instance.id)


# Создание задачи для отправки уведомлений
@shared_task
def send_new_post_notification(post_id):
    post = Post.objects.get(id=post_id)
    subscribers = Subscription.objects.filter(page=post.page, is_confirmed=True).values_list('user__email', flat=True)
    subject = f'Новая публикация на странице {post.page.title}'
    html_message = render_to_string('email/new_post_notification.html', {'post': post})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, 'from@example.com', subscribers, html_message=html_message)