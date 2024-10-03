from rest_framework import serializers
from customer.models.avis import Avis


class AvisSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Avis
        fields = "__all__"