from django import forms
from django.forms import ModelForm
from .models import Venue  # import the venue class model

# to create the form for venue

# VenueForm to be imported in views.py


class VenueForm(ModelForm):
    class Meta:  # always like this
        model = Venue  # model to use for the form
        # fields = '__all__' in you want all otherwise
        fields = ('name', 'address', 'zip_code',
                  'phone', 'web', 'email_address')
        
        # to remove labels:
        labels= {
            'name':'', 
            'address':'', 
            'zip_code':'', 
            'phone':'', 
            'web':'', 
            'email_address':'', 
        
        }  
        # from control class from bootstrap
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Zip Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Web URL'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}),
        }
