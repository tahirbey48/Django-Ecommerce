from app1.models import MockupItem
from rest_framework import serializers

class MockupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockupItem
        fields = ['title', 'price', 'category', 'description']




