
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registrarUsuario/$', views.signupPost, name='registrarUsuario'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^ingresarUsuario/$', views.loginPost, name='ingresarUsuario'),
    url(r'^gracias/$', views.thanks, name='gracias'),
]
