from django.shortcuts import render

# Create your views here.


def index(request):
    """ This view returns index page """
    return render(request, 'home/index.html')


def about_us(request):
    """ A view to return the work page to showcase designs """
    return render(request, 'home/about.html')


def exhibitions(request):
    """ A view to return the work page to showcase designs """
    return render(request, 'home/exhibitions.html')


def artists(request):
    """ A view to return the work page to showcase designs """
    return render(request, 'home/artists.html')
