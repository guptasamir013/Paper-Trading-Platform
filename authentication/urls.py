from django.urls import path
from .views import *

urlpatterns = [
    path("register/", CustomUserRegisteration, name="authentication-register"),
    path("profile/", CustomUserDetail, name="authentication-userdetail"),
    path('portfoliostock/<int:id>', PortfolioStockView, name="authentication-portfoliostock"),
    path('login/', LoginView, name="authentication-login"),
    path('logout/', LogoutView, name="authentication-logout"),
]
