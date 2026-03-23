from django import forms
from .models import info

class TumorForm(forms.ModelForm):
    class Meta:
        model = info
        fields = ['image']
    
