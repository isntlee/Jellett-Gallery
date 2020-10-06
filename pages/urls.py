from django.urls import path
from .views import artists_view, about_view, exhibitions_view

urlpatterns = [
    path('artists/', artists_view, name="artists"),
    path('about/', about_view, name="about"),
    path('exhibitions/', exhibitions_view, name="exhibitions"),
]