from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("user.urls")),
#     path("page/", include("page.urls")),
#     path("post/", include("post.urls")),
#     path("statistic/", include("statistic.urls")),
]
