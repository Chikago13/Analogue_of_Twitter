from django.contrib import admin

from .models import PageStatistic, Notification

admin.site.register(PageStatistic),
admin.site.register(Notification)
