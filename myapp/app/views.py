from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Player, Contract, Transfer
from .forms import CreateUserForm, PlayerForm


class IndexView(View):
    template_name = "app/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProfileView(View):
    template_name = "app/profile.html"

    @method_decorator(login_required(login_url='app:login'))
    def get(self, request, *args, **kwargs):
        players = Player.objects.all()  # Получаем все объекты из базы данных
        contracts = Contract.objects.all()
        transfers = Transfer.objects.all()

        player_form = PlayerForm()

        context = {
            'players': players,
            'contracts': contracts,
            'transfers': transfers,
            'player_form': player_form,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if 'player-form' in request.POST:
            player_form = PlayerForm(request.POST)
            if player_form.is_valid():
                player_form.save()

        return redirect('app:profile')


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
            return redirect('app:profile')
        else:
            messages.info(request, 'Username OR password is incorrect')

        return render(request, self.template_name)


def logout_user(request):
    logout(request)
    return redirect('app:login')
