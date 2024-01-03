from rest_framework import serializers
from .models import PageStatistic, Notification

class PageStatisticSerializers(serializers.ModelSerializer):
    class Meta:
        model = PageStatistic
        fields = '__all__'


class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        models = Notification
        fields = '__all__'