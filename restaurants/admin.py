from django.contrib import admin
from .models import Restaurant, Waiter, Place
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Place)
admin.site.register(Waiter)
