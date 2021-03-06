from django.urls import path

from .views import create_post, home, search_business, setup_profile, setup_business, biz_list, contact


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('setup-profile/', setup_profile, name='setup_profile'),
    path('setup-business/', setup_business, name='setup_business'),
    path('biz-list/', biz_list, name='biz_list'),
    path('search/', search_business, name='search_business'),
    path('create-post/', create_post, name='create_post'),

]
