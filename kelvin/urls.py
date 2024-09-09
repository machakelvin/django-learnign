# kelvin/urls.py
from django.contrib import admin
from django.urls import path, include
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name="register"),  # This URL is correct
    path("", include('main.urls')),  # Make sure 'main.urls' is correctly set up
]
