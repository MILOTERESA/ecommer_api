from rest_framework import viewsets

from customer.models.livraison import Livraison
from customer.serializers.livraison import LivraisonSerializer


class LivraisonViewSet(viewsets.ModelViewSet):
    
    queryset = Livraison.objects.filter(status=True)
    serializer_class = LivraisonSerializer