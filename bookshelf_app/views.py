from django.shortcuts import render
from .models import Item


# Create your views here.
def get_bookshelf_app(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'bookshelf_app/home.html', context)
