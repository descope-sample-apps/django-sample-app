import logging

from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views import View


logger = logging.getLogger(__name__)


class Logout(View):
    def get(self, request: HttpRequest):
        logout(request)
        return HttpResponseRedirect(reverse("index"))
