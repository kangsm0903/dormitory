"""dorm_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import dorm_app.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dorm_app.views.home, name='home'),
    path('main', dorm_app.views.main, name = 'main'),
    path('search', dorm_app.views.search, name = 'search'),
    path('apply', dorm_app. views.apply, name = 'apply'),
    path('comment', dorm_app.views.comment, name= 'comment'),
    path('room', dorm_app.views.room, name= 'room'),
    path('submit', dorm_app.views.submit, name= 'submit'),
    path('etc', dorm_app.views.etc, name = 'etc'),
    path('road', dorm_app.views.road, name = 'road'),
    path('base', dorm_app.views.base, name = 'base'),
    path('', dorm_app.views.Advice, name='advice'),
    path('new', dorm_app.views.new, name='new'),
]
