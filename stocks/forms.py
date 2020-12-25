from .models import Watchlist, WatchlistStock
from django.forms import ModelForm

class WatchListRegisterForm(ModelForm):
    class Meta:
        model = Watchlist
        fields = ["name"]

class WatchlistStockRegisterForm(ModelForm):
    class Meta:
        model = WatchlistStock
        fields = ['stock']
