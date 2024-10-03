from rest_framework import viewsets

from customer.models.client import Client
from customer.serializers.client import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    
    queryset = Client.objects.filter(status=True)
    serializer_class = ClientSerializer