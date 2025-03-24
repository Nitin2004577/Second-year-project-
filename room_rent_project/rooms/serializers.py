from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'title', 'description', 'price', 'location', 'facilities', 'photo']

    def validate_photo(self, value):
        if value and not value.startswith(('http://', 'https://')):
            raise serializers.ValidationError("Invalid URL: Must start with http:// or https://")
        return value