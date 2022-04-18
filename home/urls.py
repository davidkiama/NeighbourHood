from django.urls import path

from .views import home, search_business, setup_profile, setup_business, biz_list


urlpatterns = [
    path('', home, name='home'),
    path('setup-profile/', setup_profile, name='setup_profile'),
    path('setup-business/', setup_business, name='setup_business'),
    path('biz-list/', biz_list, name='biz_list'),
    path('search/', search_business, name='search_business'),
]
