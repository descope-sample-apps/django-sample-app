from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.views.generic import TemplateView
from .views import Logout, Summary

descope_admin_site = admin.site

# override the login template with our own
descope_admin_site.login_template = "admin_login.html"


urlpatterns = [
    path("", TemplateView.as_view(template_name="descope_login.html"), name="index"),
    path('summary/', Summary.as_view(), name='summary'),
    path('logout/', Logout.as_view(), name='logout'),
    path('auth/', include('django_descope.urls')),
    path('admin/', descope_admin_site.urls),
]
