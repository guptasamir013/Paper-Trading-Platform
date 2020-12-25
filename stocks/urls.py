from django.urls import path
from .views import *

urlpatterns = [
    path('watchlist', WatchListView, name="stocks-watchlist"),
    path('stock/<int:id>/', StockView, name="stocks-stock"),
    path('watchliststock/<int:id>/', WatchListStockView, name="stocks-watchliststock"),
    path('pendingorder/', PendingOrderView, name="stocks-pendinglist"),
    path('executedorder/', ExecutedOrderView, name="stocks-executedlist"),
    path('closeposition/<int:id>', ClosePosition, name="stocks-closeposition"),
    path('jqueryserver/<int:id>', jqueryserver, name="stocks-jqueryserver"),
]
