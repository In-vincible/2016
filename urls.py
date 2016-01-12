"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""
from django.conf.urls import include, url
from django.contrib import admin
from udyam.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view=index, name='home'),
    url(r'^(?P<page>[\w\-]+)$', view=static_page, name="p_static")
]
