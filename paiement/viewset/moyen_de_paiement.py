from rest_framework import viewsets

from paiement.models.moyen_de_paiement import MethodeDePaiement
from paiement.serializers.moyen_de_paiement import MethodeDePaiementSerializer


class MethodeDePaiementViewSet(viewsets.ModelViewSet):
    
    queryset = MethodeDePaiement.objects.filter(status=True)
    serializer_class = MethodeDePaiementSerializer