'''
Created on 03-Mar-2019

@author: sushil
'''
from django.urls import path
from app import views
from app.views import TestRunViewSet


urlpatterns = [
    path('', views.App.as_view(), name='app'),
    path('upload', views.UploadView.as_view(), name='upload'),
    path('data/upload/', TestRunViewSet.as_view(),name='data_upload'),
    path('edit_profile/', views.edit_profile,name='edit_profile'),
    path('integration/', views.integration,name='integration'),
    path('password/', views.change_password,name='change_password'),
    path('report/', views.line_chart,name='line_chart'),
    path('reports/', views.reports,name='reports'),
    path('reports/compare/testrun/', views.compare,name='compare'),
    path('reports/compare/', views.compare_reports,name='compare_reports'),
    path('reports/compare/<int:testrun_id1>/', views.compare_reports,name='compare_reports'),
    path('reports/compare/<int:testrun_id1>/<int:testrun_id2>/', views.compare_reports,name='compare_reports_full'),
    path('reports/json/', views.line_chart_json,name='line_chart_json'),
    path('tr_table/', views.tbl_testrun,name='testrun_table'),
    path('tc_table/<int:testrun_id>/', views.tbl_testcase,name='testcase_table'),
    path('ajax/testrun_list/', views.testrun_list,name='testrun_list'),
    path('rest/create_token/', views.token_request,name='create_token'),
]