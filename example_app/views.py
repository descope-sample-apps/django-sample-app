import logging

import requests
import json

from django.contrib.auth import logout
from django.urls import reverse
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


logger = logging.getLogger(__name__)


class Logout(View):
    def get(self, request: HttpRequest):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class Index(View):
    def get(self, request: HttpRequest):
        logger.info("Index view called")
        return JsonResponse(
            {
                "user": request.user.username,
                "is_authenticated": request.user.is_authenticated,
                "is_staff": request.user.is_staff,
                "is_superuser": request.user.is_superuser,
                "email": request.user.email,
            }
        )


class Memes(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        url = 'https://api.imgflip.com/get_memes'
        data = requests.get(url).json()["data"]["memes"]
        return render(request, 'memes.html', {'memes': data })

