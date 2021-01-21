from django.urls import path
from .views import (firesafetyDetailView, firesafetySearchListView)

app_name = 'firesafety'
urlpatterns = [
    path('', firesafetySearchListView.as_view(),
         name='firesafety-search-list'),
    path('<int:id>/', firesafetyDetailView.as_view(),
         name='firesafety-detail'),
]