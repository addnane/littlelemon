from django.contrib import admin
from .models import BookingTable,MenuTable


# Register your models here.
admin.site.register(BookingTable)
admin.site.register(MenuTable)