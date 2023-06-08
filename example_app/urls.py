from django.urls import path
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static

from .views import Index
from .views import Memes


urlpatterns = [
    path("", TemplateView.as_view(template_name="descope_login.html"), name="index"),
    path("memes", Memes.as_view(), name="memes"),
    path("test", Index.as_view(), name="test"),
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


