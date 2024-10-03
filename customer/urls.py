"""
URL configuration for e_com project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from .viewset.avis import AvisViewSet
from .viewset.client import ClientViewSet
from .viewset.commande import CommandeViewSet
from .viewset.livraison import LivraisonViewSet
from .viewset.panier import PanierViewSet

router = routers.DefaultRouter()
router.register(r'avis', AvisViewSet)
router.register(r'client', ClientViewSet)
router.register(r'commande', CommandeViewSet)
router.register(r'livraison', LivraisonViewSet)
router.register(r'panier', PanierViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]