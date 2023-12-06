from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm


class IndexView(View):
    template_name = "app/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegisterPage(View):
    template_name = 'app/register.html'

    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app')  # Замените 'home' на имя вашей домашней страницы
        context = {'form': form}
        return render(request, self.template_name, context)


class LoginPage(View):
    template_name = "app/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

