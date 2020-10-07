from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about_us, name='about'),
    path('exhibitions', views.exhibitions, name='exhibitions'),
    path('artists', views.artists, name='artists')
]
