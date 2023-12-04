from django.contrib import admin
from .models import Player, Club, City, Country, Contract, Transfer

# Register your models here.
admin.site.register(Player)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Contract)
admin.site.register(Club)
admin.site.register(Transfer)
