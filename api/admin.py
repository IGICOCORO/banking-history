from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
	list_display = "user", "cni", "adress","phone", "date"
	list_filter =  "user", "cni", "adress", "phone", "date"
	ordering =  "user", "cni", "adress", "phone", "date"
class Bank_AccountAdmin(admin.ModelAdmin):
	list_display = "number", "client"
	list_filter = "number", "client"
	ordering = "number", "client"

admin.site.register(Client, ClientAdmin)
admin.site.register(Bank_Account, Bank_AccountAdmin)
