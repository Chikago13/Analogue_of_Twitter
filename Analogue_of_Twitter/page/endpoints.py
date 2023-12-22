# from rest_framework import viewsets
# from .models import Page, Subscription, BlockedPage, Request
# from .serializers import PageSerializer, SubscriptionSerializer, BlockedPageSerializer, RequestSerializer
# from rest_framework.generics import ListAPIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import generics

# class PageViewSet(viewsets.ModelViewSet):
#     queryset = Page.objects.all()
#     serializer_class = PageSerializer

# class SubscriptionViewSet(viewsets.ModelViewSet):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionSerializer

# class BlockedPageViewSet(viewsets.ModelViewSet):
#     queryset = BlockedPage.objects.all()
#     serializer_class = BlockedPageSerializer

# class RequestViewSet(viewsets.ModelViewSet):
#     queryset = Request.objects.all()
#     serializer_class = RequestSerializer


# #подписаться на чужие страницы (бросить заявку на подписку в случае приватных страниц)
# #  получения списка страниц, на которые пользователь может подписаться и списка запросов на подписку:

# class SubscribePageListView(generics.ListAPIView):
#     serializer_class = PageSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         return Page.objects.exclude(subscribers=user).exclude(blockedpage=user)


# class SubscriptionRequestListView(generics.ListAPIView):
#     serializer_class = RequestSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         return Request.objects.filter(page__subscribers=user)
    

# #позволяет пользователям просматривать и создавать подписки на страницы,
# class SubscriptionListAPIView(generics.ListCreateAPIView):
#     serializer_class = SubscriptionSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         return Page.objects.filter(id=user)


# #позволяет пользователям просматривать страницы, на которые они подписаны.
# class PageSubscriptionListAPIView(generics.ListAPIView):
#     serializer_class = PageSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         return Page.objects.filter(subscribers=user)
    
# #позволяет пользователю просматривать свои ожидающие запросы  
# class PendingRequestsListAPIView(ListAPIView):
#     serializer_class = RequestSerializer

#     def get_queryset(self):
#         user = self.request.user.id
#         return Request.objects.filter(user_id=user)
