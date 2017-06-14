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
    url(r'index', views.test_cases),
    url(r'result/', views.report),
    url(r'add/', views.add),
    url(r'^save_case/$', views.add_testcase),
    url(r'^delete/$',views.delete_testcase),
    url(r'^edit/$',views.edit_testcase),
    url(r'^update_case/(?P<cid>\d+)',views.updete_testcase),
    url(r'addProject/',views.add_Project)
]
