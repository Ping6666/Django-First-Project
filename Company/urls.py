from django.urls import path
from .views import (uploadCompanyDataset, companySearchListView,
                    companySearchMapListView)

app_name = 'company'
urlpatterns = [
    path('', companySearchListView.as_view(), name='company-search-list'),
    path('map/', companySearchMapListView.as_view(),
         name='company-search-map'),
    path('uploadpath/', uploadCompanyDataset, name='company-upload'),
]