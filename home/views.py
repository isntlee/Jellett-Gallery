from django.shortcuts import render

# Create your views here.


def index(request):
    """ This view returns index page """
    return render(request, 'home/index.html')
