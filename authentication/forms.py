from django.forms import ModelForm
from django import forms
from .models import CustomUser
from stocks.models import Portfolio, PortfolioStock

class CustomUserRegister(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'occupation']

    def save(self, commit=True):
        instance = super(CustomUserRegister, self).save(commit=False)
        if instance.password is not None:
            instance.set_password(instance.password)
        instance.balance = 10000
        instance.save()
        return instance


class PortfolioRegister(ModelForm):
    class Meta:
        model = Portfolio
        fields = ["name"]

class PortfolioStockRegister(ModelForm):
    class Meta:
        model = PortfolioStock
        fields = ['stock', 'volume']
