from django.contrib import admin
from .models import Order , Type , AcademicLevel, Format



# Register your models here.

class OrderAdmin(admin.ModelAdmin):

    list_display = ("username", "type", "academic", "format", "paid", "email", )




admin.site.register(Order, OrderAdmin)

admin.site.register(Type)

admin.site.register(AcademicLevel)

admin.site.register(Format)



