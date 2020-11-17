from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from api.views import health_check


router = routers.SimpleRouter()


# router.register("url", View)


urlpatterns = [
    path('', health_check),
    path('admin', admin.site.urls),
    path('v1/', include(router.urls)),
]
