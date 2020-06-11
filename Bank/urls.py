from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('choice/bank-searching/', views.search_bank, name='search'),
    path('home/base-loading', views.load_base, name='load_base'),
    path('home/data-loading', views.load_data, name='load_data'),
    path('choice/', views.choice, name='choices'),
    path('choice/bank-searching/graph', views.chart, name='graph'),
    path('choice/text_report/report-by-date/', views.report_by_date, name='report_by_date'),
    path('choice/text_report/report-by-bank/', views.report_by_bank, name='report_by_bank'),
    path('choice/text_report/', views.text_choice, name='text_choices')
]
