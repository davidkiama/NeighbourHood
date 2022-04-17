from django.urls import path

from .views import home, setup_profile


urlpatterns = [
    path('', home, name='home'),
    path('setup-profile/', setup_profile, name='setup_profile')
]
