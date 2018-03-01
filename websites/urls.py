"""websites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from pasal import views
from base import views as base_views
from landing import views as landing_views
from services import views as services_views
from pasal import apps

app_name = apps.PasalConfig.name

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.home, name='home') , 
    #url(r'^%s/admin/'%app_name, admin.site.urls),        
    #url(r'^%s/'%app_name, views.home, name='home') ,
    #url('%s/base/'%app_name, base_views.home, name='base') , 
    url(r'%s/landing'%app_name, landing_views.home, name='landing') ,

    url(r'^$', views.home, name='home') ,     
    url(r'^pasal/', views.home, name='pasal') ,
    url(r'^base/', base_views.home, name='base') ,
    url(r'^work', base_views.base_with_work, name='work') ,
    url(r'^support', base_views.base_with_support, name='support') ,
    url(r'^service', base_views.base_with_service, name='service') ,
    url(r'^contact', base_views.base_with_contact, name='contact') ,
    
]
