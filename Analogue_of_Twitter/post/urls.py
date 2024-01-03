from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .endpoints import ( POstViewSet,
                        LikeViewSet,
)

router = DefaultRouter()
router.register(r"post", POstViewSet)
router.register(r"like", LikeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    ]