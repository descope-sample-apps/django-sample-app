import logging

from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .forms import TextForm

from summa import summarizer


logger = logging.getLogger(__name__)


class Logout(View):
    def get(self, request: HttpRequest):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class Summary(LoginRequiredMixin, View):
    login_url = "/"
    template_name = "summary.html"
    form = TextForm()

    def summarize(self, text: str) -> str:
        return summarizer.summarize(text)

    def get(self, request: HttpRequest):
        return render(request, self.template_name, {'summary_form': self.form, 'summary': ""})

    def post(self, request: HttpRequest):
        form = TextForm(request.POST)

        if form.is_valid():
            form_text=form.cleaned_data['sum_form']
            summary = self.summarize(form_text) or "Text too short!"

        return render(request, self.template_name, {'summary_form': form, 'summary': summary})