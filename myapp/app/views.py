from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Player, Contract, Transfer
from .forms import CreateUserForm, PlayerForm, TransferForm, ContractForm


class IndexView(View):
    template_name = "app/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProfileView(View):
    template_name = "app/profile.html"

    @method_decorator(login_required(login_url='app:login'))
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.handle_post_request(request)
        return redirect('app:profile')

    def get_context_data(self):
        players = Player.objects.all()
        contracts = Contract.objects.all()
        transfers = Transfer.objects.all()

        player_form = PlayerForm()
        transfer_form = TransferForm()
        contract_form = ContractForm()

        context = {
            'players': players,
            'contracts': contracts,
            'transfers': transfers,
            'player_form': player_form,
            'transfer_form': transfer_form,
            'contract_form': contract_form,
        }

        return context

    def handle_post_request(self, request):
        if 'player-form' in request.POST:
            self.handle_player_form(request.POST)

        if 'transfer-form' in request.POST:
            self.handle_transfer_form(request.POST)

        if 'contract-form' in request.POST:
            self.handle_contract_form(request.POST)

    def handle_player_form(self, post_data):
        player_form = PlayerForm(post_data)
        if player_form.is_valid():
            player_form.save()

    def handle_transfer_form(self, post_data):
        transfer_form = TransferForm(post_data)
        if transfer_form.is_valid():
            transfer_form.save()

    def handle_contract_form(self, post_data):
        contract_form = ContractForm(post_data)
        if contract_form.is_valid():
            contract_form.save()


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
