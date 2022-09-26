from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

admin.site.site_header = "Lazy Automation"
admin.site.site_title = "Lazy Automation Admin Portal"
admin.site.index_title = "Welcome to Lazy Automation Portal"
