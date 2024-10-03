from rest_framework import serializers
from customer.models.panier import Panier


class PanierSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Panier
        fields = "__all__"