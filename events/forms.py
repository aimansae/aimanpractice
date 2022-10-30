from django import forms
from django.forms import ModelForm
from .models import Venue, Event  # import the venue class model

# to create the form for venue

# VenueForm to be imported in views.py


class VenueForm(ModelForm):
    class Meta:  # always like this
        model = Venue  # model to use for the form
        # fields = '__all__' in you want all otherwise
        fields = ('name', 'address', 'zip_code',
                  'phone', 'web', 'email_address')

        # to remove labels:
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',

        }
        # from control class from bootstrap
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manager'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description '}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
        }

# for event form


class EventForm(ModelForm):
    class Meta:  # always like this
        model = Event  # model to use for the form
        # fields = '__all__' in you want all otherwise
        fields = ('name', 'event_date',
                  'venue', 'manager', 'description', 'attendees')

        # to remove labels:
        labels = {
            'name': '',
            'event_date': '',
            'venue': '',
            'manager': '',
            'description': '',
            'attendees': '',

        }
        # from control class from bootstrap
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'venue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
            'manager': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web URL'}),
            'attendees': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
