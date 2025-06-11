# serializers.py
from rest_framework import serializers
from .models import OutfitUpload, OutfitRecommendation

class OutfitUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitUpload
        fields = '__all__'

class OutfitRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitRecommendation
        fields = '__all__'
