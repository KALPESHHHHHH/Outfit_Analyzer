# # outfit_recommender/core/models.py

# from django.db import models
# from django.utils import timezone
# import os
# import json

# def outfit_image_path(instance, filename):
#     # Generate a path for the uploaded image
#     ext = filename.split('.')[-1]
#     filename = f"{timezone.now().strftime('%Y%m%d%H%M%S')}.{ext}"
#     return os.path.join('uploads', filename)

# class OutfitUpload(models.Model):
#     image = models.ImageField(upload_to=outfit_image_path)
#     uploaded_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"Outfit uploaded at {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"
    
#     @property
#     def has_recommendation(self):
#         return hasattr(self, 'recommendation')

# class OutfitRecommendation(models.Model):
#     outfit = models.OneToOneField(OutfitUpload, on_delete=models.CASCADE, related_name='recommendation')
#     looks_good = models.BooleanField(default=False)
#     feedback = models.TextField()
#     suggestions = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"Recommendation for {self.outfit}"
    
#     def set_feedback_json(self, data):
#         self.feedback = json.dumps(data)
    
#     def get_feedback_json(self):
#         return json.loads(self.feedback) if self.feedback else {}
    
#     def set_suggestions_json(self, data):
#         self.suggestions = json.dumps(data)
    
#     def get_suggestions_json(self):
#         return json.loads(self.suggestions) if self.suggestions else {}


# outfit_recommender/core/models.py

from django.db import models
from django.utils import timezone
import os
import json

def outfit_image_path(instance, filename):
    # Generate a path for the uploaded image
    ext = filename.split('.')[-1]
    filename = f"{timezone.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    return os.path.join('uploads', filename)

class OutfitUpload(models.Model):
    image = models.ImageField(upload_to=outfit_image_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Outfit uploaded at {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"
    
    @property
    def has_recommendation(self):
        return hasattr(self, 'recommendation')

class OutfitRecommendation(models.Model):
    outfit = models.OneToOneField(OutfitUpload, on_delete=models.CASCADE, related_name='recommendation')
    looks_good = models.BooleanField(default=False)
    feedback = models.TextField()
    suggestions = models.TextField()

    # ✅ New fields added
    percentage_score = models.FloatField(null=True, blank=True)
    explanation = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Recommendation for {self.outfit}"
    
    def set_feedback_json(self, data):
        self.feedback = json.dumps(data)
    
    def get_feedback_json(self):
        return json.loads(self.feedback) if self.feedback else {}
    
    def set_suggestions_json(self, data):
        self.suggestions = json.dumps(data)
    
    def get_suggestions_json(self):
        return json.loads(self.suggestions) if self.suggestions else {}
