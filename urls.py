from django.conf.urls import include, url
from django.contrib import admin
from udyam.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^adminData/',adminData, name='data'),
    url(r'^$', view=index, name='home'),
    url(r'^(?P<page>[\w\-]+)$', view=static_page, name="p_static"),
    url(r'^quiz/', include('quiz.urls'), name="quiz"),
    url(r'^signup/$', view=signup, name='signup'),
    url(r'^signup/login/', auth_views.login, {'template_name': 'login.html'},name='login'),
    url(r'^logout/', auth_views.logout,{'next_page': '/'}, name='logout'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
