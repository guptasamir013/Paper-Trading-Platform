from django.shortcuts import render, redirect
from .forms import *
from stocks.models import Portfolio
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def CustomUserRegisteration(request):
    form = CustomUserRegister()
    if request.method=="POST":
        data = request.POST
        form = CustomUserRegister(data=data)
        if form.is_valid():
            instance = form.save()
            return HttpResponse("Hello")
    return render(request, "authentication/register.html", {'form':form})

def CustomUserDetail(request):
    user = request.user
    portfoliolist = Portfolio.objects.filter(owner=user)
    if request.method=="POST":
        data = request.POST
        form = PortfolioRegister(data=data)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
    form = PortfolioRegister()
    return render(request, "authentication/userdetail.html/", {"user":user, 'portfoliolist':portfoliolist, 'form':form})


def PortfolioStockView(request, id):
    try:
        portfoliolist = Portfolio.objects.filter(owner=request.user).get(id=id)
        portfoliostock = PortfolioStock.objects.filter(portfolio=portfoliolist)
        form = PortfolioStockRegister()
        if request.method=="POST":
            form = PortfolioStockRegister(data=request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.portfolio = portfoliolist
                instance.save()
        return render(request, 'authentication/portfoliostock.html/', {'portfoliostock':portfoliostock, 'form':form})
    except:
        return HttpResponse('Not Found')

def LoginView(request):
    context = {}
    if request.method=="POST":
        data = request.POST
        user = authenticate(username=data["username"], password=data["password"])
        if user is not None:
            login(request, user)
            return redirect("stocks-watchlist")
        else:
            print("Wrong Credentials")
            context["error"] = "Wrong Credentials"

    return render(request, "authentication/login.html", context)

def LogoutView(request):
    logout(request)
    return redirect("authentication-login")
