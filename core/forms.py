# outfit_recommender/core/forms.py

from django import forms
from .models import OutfitUpload

class OutfitUploadForm(forms.ModelForm):
    class Meta:
        model = OutfitUpload
        fields = ['image']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*',
        })
        self.fields['image'].label = 'Upload your outfit image'