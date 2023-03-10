from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(ExpenseUser)
admin.site.register(PocketMoney)
admin.site.register(Budget)