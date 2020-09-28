from django.urls import path
from home.views import go_to, home_page, show_url

urlpatterns = [
    path('<slug:slug>', go_to, name='home'),
    path('', home_page, name='homepage'),
    path('short/', show_url)
]
