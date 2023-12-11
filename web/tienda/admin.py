from django.contrib import admin
from .models import categoria, producto
# Register your models here.


class categoria_admin(admin.ModelAdmin):
    readonly_fields = ('created',)
    
class producto_admin(admin.ModelAdmin):
    readonly_fields =("created",)
    
admin.site.register(producto, producto_admin)
admin.site.register(categoria, categoria_admin)