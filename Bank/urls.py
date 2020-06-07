from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('choice/bank-searching/', views.search_bank, name='search'),
    path('home/', views.load, name='load'),
    path('choice/', views.choice, name='choices'),
    path(r'choice/bank-searching/graph', views.chart, name='graph')
]
