from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .endpoints import PageViewSet, SubscriptionViewSet, BlockedPageViewSet, RequestViewSet, SubscriptionListAPIView, SubscribeToPage, PageSubscriptionListAPIView, PendingRequestsListAPIView, RequestSubscriptionToPrivatePage


router = DefaultRouter()

router.register(r'pages', PageViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'blocked-pages', BlockedPageViewSet)
router.register(r'requests', RequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('subscribe/', SubscriptionListAPIView.as_view(), name='subscribe'),
    path('subscribe-page/', SubscribeToPage.as_view(), name='subscribe-page'),
    path('page-subscription/', PageSubscriptionListAPIView.as_view(), name='page-subscription'),
    path('pending-requests/', PendingRequestsListAPIView.as_view(), name='pending-requests'),
    path('requests-subscription/', RequestSubscriptionToPrivatePage.as_view(), name='requests-subscription'),
]