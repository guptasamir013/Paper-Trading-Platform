from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Watchlist)
admin.site.register(Stock)
admin.site.register(PendingOrder)
admin.site.register(ExecutedOrder)
admin.site.register(WatchlistStock)
