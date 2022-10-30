from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Venue(models.Model): #fields to use in form too
    # not necessary to name
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=15,blank=True ) 
    phone = models.CharField('Contact Phone', max_length=15, blank=True)
    web = models.URLField('Website Address', max_length=200, blank=True)
    email_address = models.EmailField('Email')

# to use the model in the admin area


    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField('User Email')


    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    # not necessary to name
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    # venue = models.CharField(max_length=120) # not necessary to name
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=120)  # not necessary to name
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
# to use the model in the admin area


    def __str__(self):
        return self.name
