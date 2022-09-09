from django.contrib import admin
from .models import Exchange, Coins, Network

# Register your models here.


class ExchangeAdmin(admin.ModelAdmin):
    list_display = ['name']


class CoinsAdmin(admin.ModelAdmin):
    list_display = ['name']


class NetworkAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(Coins, CoinsAdmin)
admin.site.register(Network, NetworkAdmin)
