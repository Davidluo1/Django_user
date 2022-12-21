from rest_framework import serializers

class AddReactionRequest(serializers.Serializer):
    reaction = serializers.CharField(max_length = 100)