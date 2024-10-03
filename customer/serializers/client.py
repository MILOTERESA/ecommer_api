from rest_framework import serializers
from customer.models.client import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"