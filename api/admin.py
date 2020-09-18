from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
	list_display = "user", "cni", "adress","phone", "date"
	list_filter =  "user", "cni", "adress", "phone", "date"
	ordering =  "user", "cni", "adress", "phone", "date"

class BankAccountAdmin(admin.ModelAdmin):
	list_display = "number","balance"
	list_filter = "number", "client","balance"
	ordering = "number", "client","balance"

class ActionAdmin(admin.ModelAdmin):
	list_display = "bank_account", "montant", "date", "motif"
	list_filter = "bank_account", "montant", "date", "motif"
	ordering = "bank_account", "montant", "date", "motif"

admin.site.register(Client, ClientAdmin)
admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(Action, ActionAdmin)
