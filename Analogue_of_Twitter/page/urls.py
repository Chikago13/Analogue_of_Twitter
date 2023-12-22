# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .endpoints import PageViewSet, SubscriptionViewSet, BlockedPageViewSet, RequestViewSet, SubscribePageListView, SubscriptionRequestListView, PageSubscriptionListAPIView, SubscriptionListAPIView, PendingRequestsListAPIView
# router = DefaultRouter()
# router.register(r'pages', PageViewSet)
# router.register(r'subscriptions', SubscriptionViewSet)
# router.register(r'blocked-pages', BlockedPageViewSet)
# router.register(r'requests', RequestViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('subscribe-pages/', SubscribePageListView.as_view(), name='subscribe-pages'),
#     path('subscription-requests/', SubscriptionRequestListView.as_view(), name='subscription-requests'),
#     path('page-subscription/', PageSubscriptionListAPIView.as_view(), name='page-subscription'),
#     path('subscription/', SubscriptionListAPIView.as_view(), name='subscription'),
#     path('pending-requests/', PendingRequestsListAPIView.as_view(), name='pending-requests'),
# ]