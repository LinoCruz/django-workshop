from django import forms
from .models import Construction

class ConstructionForm(forms.ModelForm):
    class Meta:
        model = Construction
        fields='__all__'
        exclude = ['created_at', 'updated_at']