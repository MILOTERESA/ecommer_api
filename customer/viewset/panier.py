from rest_framework import viewsets

from customer.models.panier import Panier
from customer.serializers.panier import PanierSerializer


class PanierViewSet(viewsets.ModelViewSet):
    
    queryset = Panier.objects.filter(status=True)
    serializer_class = PanierSerializer