from django.shortcuts import render_to_response
from simple_vxml_menu.models import Menu, MenuItem
from django.http import Http404

def vxml_file(request, slug):
    try:
        menu = Menu.objects.get(slug=slug)
    except:
        raise Http404()

    menu_items = MenuItem.objects.filter(menu=menu)

    if not menu_items:
        raise Http404()

    return render_to_response('simple_vxml_menu/vxml.xml', {'menu': menu, 'menu_items': menu_items}, mimetype = 'text/xml')
