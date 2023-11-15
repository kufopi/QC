from django.forms import ModelForm,Textarea
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserProfile(forms.ModelForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ('username', 'email')



class UserForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

class StaffForm(forms.ModelForm):
    
    class Meta:
        model = Staff
        exclude = ['registration_date','user']
        widgets = {
            'dob':  forms.DateInput(attrs={'type':'date'}),
            'doe':  forms.DateInput(attrs={'type':'date'}),
        }


class PublicationForm(forms.ModelForm):
    
    class Meta:
        model = Publication
        exclude = ['reg_date','user']
        widgets = {
            'publication_date':  forms.DateInput(attrs={'type':'date'}),
            'co_authors':  Textarea(attrs={'cols': 8, 'rows': 2}),
            'abstract': Textarea(attrs={'cols': 8, 'rows': 2}),
            
        }

class ConferenceForm(forms.ModelForm):
    
    class Meta:
        model = Conference
        
        exclude = ['reg_date','user']
        widgets = {
            'conference_date':  forms.DateInput(attrs={'type':'date'}),
            'abstract':  Textarea(attrs={'cols': 8, 'rows': 3}),
            
            
        }


class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        exclude = ['user']
        widgets = {
           
            'co_authors':  Textarea(attrs={'cols': 8, 'rows': 2}),
            
            
        }


class PromotionForm(forms.ModelForm):
    
    class Meta:
        model = Promotion
        exclude = ['user']
        widgets = {
            'promotion_date':  forms.DateInput(attrs={'type':'date'}),
            
        }


class searchform(forms.Form):
    pub_number = forms.IntegerField( required=True)
    conf_number = forms.IntegerField(required=True)
    book_number = forms.IntegerField(required=True)

    """search definition."""

    # TODO: Define form fields here




