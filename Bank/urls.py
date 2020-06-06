from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('choice/bank-searching/', views.search_bank, name='search'),
    path('home/', views.load, name='load'),
    path('choice/', views.choice, name='choices'),
    path('choice/bank-searching/graph', views.graph, name='graph')
]
