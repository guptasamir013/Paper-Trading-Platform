from django.db import models
from authentication.models import CustomUser

# Create your models here.
class Watchlist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class WatchlistStock(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.stock.name

class PendingOrder(models.Model):
    typelist = (("buy", "buy"), ("sell", "sell"))
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    open_price = models.IntegerField()
    volume = models.IntegerField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    type = models.CharField(choices=typelist, max_length=10, default="buy")

    def __str__(self):
        return self.stock.name + " " + str(self.volume)

class ExecutedOrder(models.Model):
    typelist = (("buy-sell", "buy-sell"), ("sell-buy", "sell-buy"))
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    open_price = models.IntegerField()
    close_price = models.IntegerField()
    volume = models.IntegerField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    type = models.CharField(choices=typelist, max_length=10, default="buy-sell")

    def __str__(self):
        return self.stock.name + " " + str(self.volume)

class Portfolio(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class PortfolioStock(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    volume = models.IntegerField(default=0)

    def __str__(self):
        return self.stock.name
