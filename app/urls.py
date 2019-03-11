'''
Created on 03-Mar-2019

@author: sushil
'''
from django.urls import path
from app import views


urlpatterns = [
    path('', views.App.as_view(), name='app'),
    path('upload', views.UploadView.as_view(), name='upload'),
    path('report/', views.line_chart,name='line_chart'),
    path('reports/', views.reports,name='reports'),
    path('reports/compare/', views.compare_reports,name='compare'),
    path('reports/compare/<int:testrun_id1>/', views.compare_reports,name='compare_reports'),
    path('reports/compare/<int:testrun_id1>/<int:testrun_id2>/', views.compare_reports,name='compare_reports_full'),
    path('reports/json/', views.line_chart_json,name='line_chart_json'),
    path('tr_table/', views.tbl_testrun,name='testrun_table'),
    path('tc_table/<int:testrun_id>/', views.tbl_testcase,name='testcase_table'),
]