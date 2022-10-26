from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
# for copyright year
from datetime import datetime

# Create your views here.


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
