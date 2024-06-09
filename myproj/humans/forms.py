from django import forms
from .models import Humans
import re
from django.core.exceptions import ValidationError
class PersonForm(forms.ModelForm): 
    def clean_nicname(self):
        nicname = self.cleaned_data['nicname']
        if re.match(r'^\d', nicname):
            raise ValidationError('Название не должно начинаться с цифры')
        return nicname
    
    class Meta:
        model = Humans
        fields = ['nicname','famil','name','otches','birthday','ismale','profession','avatar'] 
        widgets = {
            'nicname': forms.TextInput(attrs={'class': 'form-control'}),
            'famil': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'otches': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'ismale': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'profession': forms.Select(attrs={'class': 'form-select'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }