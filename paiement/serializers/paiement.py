from rest_framework import serializers
from paiement.models.paiement import Paiement


class PaiementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Paiement
        fields = "__all__"