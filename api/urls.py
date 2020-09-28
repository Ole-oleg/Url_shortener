from django.urls import path
from api.views import shortener

urlpatterns = [
    path('', shortener)
]
