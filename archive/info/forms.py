from django.forms import ModelForm
from .models import Student
from django import forms


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        exclude = ['date_reg']
        widgets = {
            'DoB': forms.DateInput(attrs={'type':'date'}),
        }
