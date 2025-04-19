# outfit_recommender/core/admin.py

from django.contrib import admin
from .models import OutfitUpload, OutfitRecommendation

class OutfitRecommendationInline(admin.StackedInline):
    model = OutfitRecommendation
    readonly_fields = ('created_at',)
    extra = 0

@admin.register(OutfitUpload)
class OutfitUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at', 'has_recommendation')
    list_filter = ('uploaded_at',)
    search_fields = ('id',)
    inlines = [OutfitRecommendationInline]

@admin.register(OutfitRecommendation)
class OutfitRecommendationAdmin(admin.ModelAdmin):
    list_display = ('id', 'outfit', 'looks_good', 'created_at')
    list_filter = ('looks_good', 'created_at')
    search_fields = ('outfit__id',)
    readonly_fields = ('created_at',)