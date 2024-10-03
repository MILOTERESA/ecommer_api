from rest_framework import viewsets

from customer.models.avis import Avis
from customer.serializers.avis import AvisSerializer


class AvisViewSet(viewsets.ModelViewSet):
    
    queryset = Avis.objects.filter(status=True)
    serializer_class = AvisSerializer