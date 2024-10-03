from rest_framework import serializers
from paiement.models.moyen_de_paiement import MethodeDePaiement


class MethodeDePaiementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MethodeDePaiement
        fields = "__all__"