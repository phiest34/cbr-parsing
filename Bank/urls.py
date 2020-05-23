from django.urls import path
from . import views
from . import models
urlpatterns = [
    path('', views.index, name="home"),
    path('bank-searching/', views.search_bank),
    path('month-searching/', views.load),
    path('choice/', views.choice, name='choices')
]