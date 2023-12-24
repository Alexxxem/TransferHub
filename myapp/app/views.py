from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Player, Contract, Transfer, Country
from .forms import CreateUserForm, PlayerForm, TransferForm, ContractForm
from .decorators import unauthenticated_user


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
        countries = Country.objects.all()

        player_form = PlayerForm()
        transfer_form = TransferForm()
        contract_form = ContractForm()

        context = {
            'players': players,
            'contracts': contracts,
            'transfers': transfers,
            'countries': countries,
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


def update_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('app:profile')
    else:
        form = PlayerForm(instance=player)

    context = {
        "form": form,
    }
    return render(request, 'app/update_form.html', context)


def update_contract(request, pk):
    contract = get_object_or_404(Contract, contract_id=pk)

    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('app:profile')
    else:
        form = ContractForm(instance=contract)

    context = {
        "form": form,
    }
    return render(request, 'app/update_form.html', context)


def update_transfer(request, pk):
    transfer = get_object_or_404(Transfer, transfer_id=pk)

    if request.method == 'POST':
        form = TransferForm(request.POST, instance=transfer)
        if form.is_valid():
            form.save()
            return redirect('app:profile')
    else:
        form = TransferForm(instance=transfer)

    context = {
        "form": form,
    }
    return render(request, 'app/update_form.html', context)


def delete_player(request, pk):
    player = get_object_or_404(Player, pk=pk)

    if request.method == 'POST':
        player.delete()
        return redirect('app:profile')

    context = {
        'player': player,
    }
    return render(request, 'app/delete.html', context)


def delete_contract(request, pk):
    contract = get_object_or_404(Contract, pk=pk)

    if request.method == 'POST':
        contract.delete()
        return redirect('app:profile')

    context = {
        'contract': contract,
    }
    return render(request, 'app/delete.html', context)


def delete_transfer(request, pk):
    transfer = get_object_or_404(Transfer, pk=pk)

    if request.method == 'POST':
        transfer.delete()
        return redirect('app:profile')

    context = {
        'contract': transfer,
    }
    return render(request, 'app/delete.html', context)


class RegisterPage(View):
    template_name = 'app/register.html'

    @method_decorator(unauthenticated_user)
    def get(self, request):
        form = CreateUserForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    @method_decorator(unauthenticated_user)
    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('app:login')
        context = {'form': form}
        return render(request, self.template_name, context)


# @unauthenticated_user
class LoginPage(View):
    template_name = "app/login.html"

    @method_decorator(unauthenticated_user)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @method_decorator(unauthenticated_user)
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


def delete_object(request, model, pk):
    model_class = {
        'player': Player,
        'contract': Contract,
        'transfer': Transfer,
    }.get(model)

    obj = get_object_or_404(model_class, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('app:profile')

    context = {
        'object': obj,
        'model_type': model,
    }
    return render(request, 'app/delete.html', context)
