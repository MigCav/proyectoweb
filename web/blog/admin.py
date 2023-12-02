from django.contrib import admin
from .models import categoria, post

# Register your models here.

class postadmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
    
class categoriaadmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
    
admin.site.register(post, postadmin)
admin.site.register(categoria, categoriaadmin)
