from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm


class IndexView(View):
    template_name = "app/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProfileView(View):
    template_name = "app/profile.html"

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
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('app:login')
        context = {'form': form}
        return render(request, self.template_name, context)


class LoginPage(View):
    template_name = "app/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('app:index')
        else:
            messages.info(request, 'Username OR password is incorrect')

        return render(request, self.template_name)


def logout_user(request):
    logout(request)
    return redirect('app:login')


