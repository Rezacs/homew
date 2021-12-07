from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Address)

# Register your models here.
