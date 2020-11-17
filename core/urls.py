from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from api.views import (InvoiceViewSet, TemplateViewSet,
                       ClientCompanyViewSet, LineViewSet,
                       ClientParticularViewSet)
from api.views import health_check



router = routers.SimpleRouter()

router.register("invoices", InvoiceViewSet)
router.register("templates", TemplateViewSet)
router.register("lines", LineViewSet)
router.register("clients/particulars", ClientCompanyViewSet)
router.register("clients/companies", ClientParticularViewSet)


urlpatterns = [
    path('', health_check),
    path('admin', admin.site.urls),
    path('v1/', include(router.urls)),
]
