from rest_framework import serializers


class NumberSerializer(serializers.Serializer):
    value = serializers.CharField()

