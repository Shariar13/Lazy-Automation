from django.urls import path
from .views import (
    home,
    virtual_assistant,
)

urlpatterns = [

    path('', home, name='home'),
    path('virtual_assistant', virtual_assistant, name='virtual_assistant'),
]
