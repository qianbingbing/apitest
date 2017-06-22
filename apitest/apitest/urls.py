"""apitest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from testcase import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^login_action/$', views.login_action),
    url(r'index', views.index),
    url(r'result/', views.report_list),
    url(r'add_interface/', views.add_interface),
    url(r'^save_interface/$', views.save_interface),
    url(r'^delete_interface/$',views.delete_interface),
    url(r'^edit_interface/$',views.edit_interface),
    url(r'^update_interface/(?P<cid>\d+)',views.update_interface),
    url(r'save_project/$',views.save_project),
    url(r'^project.html/$',views.project),
    url(r'addProject/',views.add_Project),
    url(r'^case_list/$',views.case_list),
    url(r'add_testcase/', views.add_testcase),
    url(r'save_testcase/', views.save_testcase),
    url(r'^run_test/$', views.run_test),
    url(r'delete_testcase/', views.delete_testcase),
    url(r'edit_testcase/', views.edit_testcase),
    url(r'update_testcase/', views.update_testcase),
    url(r'report_detail/',views.report_detail),
    url(r'cases_detail/',views.cases_detail)
]
