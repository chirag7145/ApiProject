from django.contrib import admin

# Register your models here.

from .models import Pizza,Size,Topping


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('type', 'size', 'topping')
    list_filter = ('size','topping')
admin.site.register(Size)
admin.site.register(Topping)
