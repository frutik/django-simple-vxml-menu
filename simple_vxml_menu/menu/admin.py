from menu.models import Menu, MenuItem
from django.contrib import admin

class MenuAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Menu, MenuAdmin)

class MenuItemAdmin(admin.ModelAdmin):
    list_display_links = list_display = ('menu', 'title')
    list_filter = ('menu',)
    
admin.site.register(MenuItem, MenuItemAdmin)

