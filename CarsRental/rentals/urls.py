from django.urls import path
from . import views
app_name='rentals'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('info/', views.info, name='info')
]