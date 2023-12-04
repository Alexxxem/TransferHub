from django.shortcuts import render
from django.views import View
from .models import Player


class IndexView(View):
    template_name = "app/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
