"""obie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from carriersearch.views import *

router = routers.DefaultRouter()
# router.register(r'states', views.StateViewSet)
# router.register(r'policies', views.PolicySerializer)
# router.register(r'carriers', views.CarrierSerializer)
# router.register(r'offerings', views.OfferingSerializer)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("states/", StateList.as_view(), name="state_list"),
    path("policies/", PolicyList.as_view(), name="policy_list"),
    path("carriers/", CarrierList.as_view(), name="carrier_list"),
    path("offerings/", OfferingList.as_view(), name="offering_list"),
]
