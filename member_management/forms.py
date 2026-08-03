from django import forms
from .models import members

class abc(forms.ModelForm):
    class Meta:
        model = members
        fields = '__all__'