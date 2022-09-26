from django.urls import path
from .views import (
    home,
    virtual_assistant,
    search_youtube,
)

urlpatterns = [

    path('', home, name='home'),
    path('virtual_assistant', virtual_assistant, name='virtual_assistant'),
    path('search_youtube', search_youtube, name='search_youtube'),
]
