"""NurtureLabAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from webapi import views
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    url(r'^user/(?P<id>\d+)/advisor/$', views.AdvisorList.as_view()),
    url(r'^user/(?P<id>\d+)/advisor/booking/$', views.AdvisorBookedList.as_view()),
    path('user/register/', views.RegisterAPI.as_view()),
    path('user/login/', views.LoginAPI.as_view()),
    url(r'^user/(?P<id>\d+)/advisor/(?P<adv_id>\d+)/$', views.BookCallAdvisor.as_view()),

]

