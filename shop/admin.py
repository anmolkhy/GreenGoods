from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Item)
admin.site.register(User)
admin.site.register(ItemInventory)
admin.site.register(Order)
admin.site.register(CartObject)