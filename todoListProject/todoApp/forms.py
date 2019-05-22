from django.forms import ModelForm
from .models import todoModel
from django import forms

class todoModelForm(forms.ModelForm):
    class Meta:
        model=todoModel
        fields='__all__'