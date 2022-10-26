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
]
