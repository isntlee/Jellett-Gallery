from django.shortcuts import render
# from products.models import Product


# Create your views here.
def about_view(request, *args, **kwargs):
    return render(request, "about.html", {"page": "about"})


def artists_view(request, *args, **kwargs):
    return render(request, "artists.html", {"page": "about"})


def exhibitions_view(request, *args, **kwargs):
    return render(request, "exhbitions.html", {"page": "about"})
