from rest_framework import viewsets

from customer.models.commande import Commande
from customer.serializers.commande import CommandeSerializer


class CommandeViewSet(viewsets.ModelViewSet):
    
    queryset = Commande.objects.filter(status=True)
    serializer_class = CommandeSerializer