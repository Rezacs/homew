from django.contrib import admin

from .models import *

# admin.site.register(Basket)
# admin.site.register(Order)
# admin.site.register(Email_response)

admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(Order)
admin.site.register(Email_response)

# Register your models here.
