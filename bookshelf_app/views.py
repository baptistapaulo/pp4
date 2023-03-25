from django.shortcuts import render

# Create your views here.
def get_bookshelf_app(request):
    return render(request, 'bookshelf_app/home.html')