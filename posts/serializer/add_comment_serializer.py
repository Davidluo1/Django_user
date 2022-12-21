from rest_framework import serializers

class AddCommentRequest(serializers.Serializer):
    comment = serializers.CharField(max_length = 100)