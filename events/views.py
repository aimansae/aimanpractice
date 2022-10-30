from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
# for copyright year
from datetime import datetime
# to pull data from admin table to all_events function
# for the form to redirect the page
from django.http import HttpResponseRedirect

from .models import Event
# import the venue form created
from .forms import VenueForm



def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_venue.html',
                  {'form': form, 'submitted': submitted})

# Create your views here.


def all_events(request):
    # to pull data from admint table to this function
    # create a variable, call the table and assign .objects.all()
    event_list = Event.objects.all()
    # return the content to event_list template
    # now pass this event_list variable to our web page**
    # now we reference 'event_list' on events_list.html page

    return render(request, 'events_list.html', {'event_list': event_list})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):  # %B for month
    name = 'jhon'  # for context dictionary {}
    month = month.title()  # to convert month in upper lower

    # or month = month.capitalizes()

    # convert month to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    # create calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )
    # get current year
    now = datetime.now()
    current_year = now.year

    # get current time

    time = now.strftime('%H:%M:%S %p')  # or %I(3:00)
    return render(request, 'home.html', {
        # first_name= to be referenced in html   //   # name= variable from above
        'first_name': name,
        # to pass the year and month put them in dictionary
        'year': year,  # year and month comes form top
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'current_year':  current_year,
        'time': time


    })
