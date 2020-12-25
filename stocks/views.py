from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.

def WatchListView(request):
    watchlist = Watchlist.objects.filter(owner=request.user)
    if request.method=="POST":
        data = request.POST
        form = WatchListRegisterForm(data=data)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
    form = WatchListRegisterForm()
    return render(request, "stocks/watchlist.html/", {'watchlist':watchlist, 'form':form})

def WatchListStockView(request, id):
    try:
        watchlist = Watchlist.objects.filter(owner=request.user).get(id=id)
        watchlistStock = WatchlistStock.objects.filter(watchlist=watchlist)
        form = WatchlistStockRegisterForm()
        if request.method=="POST":
            form = WatchlistStockRegisterForm(data=request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.watchlist = watchlist
                instance.save()
        return render(request, 'stocks/watchliststock.html/', {'watchlistStock':watchlistStock, 'form':form})
    except:
        return HttpResponse('Not Found')


def predict(stock):
    print("Hi")
    return "UP"

def jqueryserver(request, id):
    try:
        stock = Stock.objects.get(id=id)
        response_string=predict(stock)
        if request.method == 'GET':
            if request.is_ajax()== True:
                return HttpResponse(response_string)
    except:
        return HttpResponse("Not Found")

def StockView(request, id):
    try:
        stock = Stock.objects.get(id=id)
        if request.method=="POST":
            user = request.user
            data = request.POST
            instance = PendingOrder(stock=stock, open_price=float(data["current_price"]), volume=float(data["volume"]), owner=user)
            if "buy" in data:
                instance.type = "buy"
            else:
                instance.type = "sell"
            if user.balance>=instance.volume * instance.open_price:
                instance.save()
                user.balance -= instance.volume * instance.open_price
                user.save()
            else:
                return HttpResponse('Insufficient Balance')
        return render(request, "stocks/stock.html/", {'stock':stock})
    except:
        return HttpResponse('Not Found')

def PendingOrderView(request):
    pendinglist = PendingOrder.objects.filter(owner=request.user)
    return render(request, 'stocks/pendingorder.html/', {'pendinglist':pendinglist})

def ClosePosition(request, id):
    try:
        order = PendingOrder.objects.filter(owner=request.user).get(id=id)
        user = request.user
        if request.method=="POST":
            current_price = request.POST["current_price"]
            net = (float(current_price) - order.open_price)
            executed_order = ExecutedOrder(stock=order.stock, volume=order.volume, open_price=order.open_price, close_price=float(current_price), owner=user)
            if order.type=="buy":
                user.balance += executed_order.volume*(order.open_price + net)
                executed_order.type = "buy-sell"
            else:
                user.balance += executed_order.volume*(order.open_price - net)
                executed_order.type = "sell-buy"
            executed_order.save()
            user.save()
            order.delete()
        pendinglist = PendingOrder.objects.filter(owner=request.user)
        return render(request, 'stocks/pendingorder.html/', {'pendinglist':pendinglist})
    except:
        return HttpResponse('Not Found')


def ExecutedOrderView(request):
    executedlist = ExecutedOrder.objects.filter(owner=request.user)
    return render(request, 'stocks/executedorder.html/', {'executedlist':executedlist})
