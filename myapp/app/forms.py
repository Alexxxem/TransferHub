from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Player, Contract, Transfer


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
