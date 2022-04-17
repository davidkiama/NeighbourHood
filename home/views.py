from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

from .models import Profile

# Create your views here.

# Helper function to create profile


# def get_profile(user):
#     try:
#         # If profile is created, get the profile
#         profile = Profile.objects.get(user=user)
#     except Profile.DoesNotExist:
#         # If profile is not created, create a new profile
#         profile = Profile(user=user)
#         profile.save_user()

#     return profile


def home(request):
    return render(request, 'index.html')


def setup_profile(request):
    return render(request, 'setup_profile.html')
