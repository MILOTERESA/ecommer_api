from rest_framework import serializers
from customer.models.commande import Commande


class CommandeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Commande
        fields = "__all__"