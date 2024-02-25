from rest_framework import serializers
from quickstart.models import Branch

class BranchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=200)
    operating_hours = serializers.CharField(max_length=200)
    waze_link = serializers.CharField(max_length=400)
    latitude = serializers.CharField(max_length=20)
    longitude = serializers.CharField(max_length=20)

    def create(self, validated_data):
        """Create new Branch instance with validated data."""
        return Branch.objects.create(**validated_data)
    