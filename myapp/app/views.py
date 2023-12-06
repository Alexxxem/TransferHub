from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm


class IndexView(View):
    template_name = "app/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegisterPage(View):
    template_name = 'app/register.html'

    def get(self, request):
        form = CreateUserForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:register')
        context = {'form': form}
        return render(request, self.template_name, context)


class LoginPage(View):
    template_name = "app/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

