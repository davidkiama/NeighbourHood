from django.urls import path

from .views import home, setup_profile, setup_business


urlpatterns = [
    path('', home, name='home'),
    path('setup-profile/', setup_profile, name='setup_profile'),
    path('setup-business/', setup_business, name='setup_business')


]
