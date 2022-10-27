from django.contrib import admin
from .models import Venue, MyClubUser, Event  # table names


# Register your models here.
# admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')  # coming from Venue Model
    # to order, descending order: ('-name',)
    ordering = ('name',)  # this is a tuple, put comma
    # for serach box
    search_fields = ('name', 'address')
