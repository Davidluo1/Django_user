from rest_framework import serializers

class AddGerneRequest(serializers.Serializer):
    gerne = serializers.CharField(max_length = 100)