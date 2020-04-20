from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    fields = ('name',)


@admin.register(Offering)
class OfferingAdmin(admin.ModelAdmin):
    fields = ('carrier', 'state', 'policy',)


@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    fields = ('name',)


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    fields = ('name',)
