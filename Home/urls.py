from django.urls import path

from .views import homepagesListView

app_name = 'homepage'
urlpatterns = [
    path('', homepagesListView.as_view(), name='homepage-list'),
]