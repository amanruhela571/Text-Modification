"""demoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from home import views

urlpatterns = [
    path('',views.index,name='index'),  # add ( or 'home' )
    path('home',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('newpage',views.newpage,name='newpage'),
    path('analyze',views.analyze,name='analyze')
]


# pipeline is just have function in views.py for thier corresponding parh in urls.py
