from rest_framework import serializers
from .models import Page, Subscription, BlockedPage, Request

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class BlockedPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedPage
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    subscribers = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #может использоваться для представления цели отношения с использованием его первичного ключа.

    class Meta:
        model = Page
        fields = '__all__'