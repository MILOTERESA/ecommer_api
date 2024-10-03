from rest_framework import serializers
from customer.models.livraison import Livraison


class LivraisonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Livraison
        fields = "__all__"