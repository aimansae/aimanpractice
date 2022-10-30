from django.urls import path
# . means same directory

from .import views
urlpatterns = [
    # '<>' : path convertors
    # int : numbers
    # str : strings
    # path : entire urls
    # slug (hiphen - , underscore_, )
    # UUID : universally unique identifier

    path('', views.home, name='home'),  # with SLASH /
    path('<int:year>/<str:month>/', views.home, name='home'),
    # name to be used in html url href
    path('events/', views.all_events, name='list-events'),
    # add_venue function to be created in views.py, name to use in html
    path('add_venue/', views.add_venue, name='add-venue'),
    path('list_venues/', views.list_venues, name='list-venues'),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('search_venues/', views.search_venues, name='search-venues'),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
    path('add_event/', views.add_event, name='add-event'),

]
