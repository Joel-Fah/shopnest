from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('search/', views.search_view, name='search'),
]
