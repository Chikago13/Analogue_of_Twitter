from rest_framework import viewsets
from .models import Page, Subscription, BlockedPage, Request
from .serializers import PageSerializer, SubscriptionSerializer, BlockedPageSerializer, RequestSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class BlockedPageViewSet(viewsets.ModelViewSet):
    queryset = BlockedPage.objects.all()
    serializer_class = BlockedPageSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


#подписаться на чужие страницы (бросить заявку на подписку в случае приватных страниц)


class SubscriptionListAPIView(ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Subscription.objects.filter(page=user)
    

class SubscribeToPage(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self):
        user = self.request.user
        page_id = self.kwargs['pk']
        page = Page.objects.get(id=page_id)
        subscription = Subscription.objects.create(subscriber=user, page=page)
        return subscription
    
# Endpoint для отправки заявки на подписку на приватную страницу
class RequestSubscriptionToPrivatePage(CreateAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        page_id = request.data.get('page_id')
        page = get_object_or_404(Page, id=page_id, is_private=True)
        request = Request.objects.create(user=user, page=page)
        return Response({'success': True})
    

#позволяет пользователям просматривать страницы, на которые они подписаны.
class PageSubscriptionListAPIView(generics.ListAPIView):
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Page.objects.filter(subscribers=user)
    
#позволяет пользователю просматривать свои ожидающие запросы  
class PendingRequestsListAPIView(ListAPIView):
    serializer_class = RequestSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Request.objects.filter(user_id=user)