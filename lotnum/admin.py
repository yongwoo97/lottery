from django.contrib import admin
from . import models

@admin.register(models.LotteryNumber)
class NumberAdmin(admin.ModelAdmin):
    list_display = (
        'number', 'date', 'n1', 'n2', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7'
    )
    list_display_links = (
        'number',
    )
# Register your models here.
