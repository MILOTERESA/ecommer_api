from rest_framework import viewsets

from paiement.models.paiement import Paiement
from paiement.serializers.paiement import PaiementSerializer


class PaiementViewSet(viewsets.ModelViewSet):
    
    queryset = Paiement.objects.filter(status=True)
    serializer_class = PaiementSerializer