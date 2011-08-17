from menu.models import Menu, MenuItem
from django.contrib import admin

class MenuAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Menu, MenuAdmin)

class MenuItemAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(MenuItem, MenuItemAdmin)

