from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('choice/bank-searching/', views.search_bank),
    path('home/', views.load, name='load'),
    path('choice/', views.choice, name='choices'),
    path('choice/bank-searching/graph', views.get_graph, name='graph')
]
