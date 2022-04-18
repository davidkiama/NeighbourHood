
from unicodedata import name
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Profile, Neighbourhood, Business

# Create your views here.

# Helper function to create profile


def home(request):
    return render(request, 'index.html')


def get_or_create_neighbourhood(request):

    neigh_name = request.POST['neighbourhood_name']
    neigh_loc = request.POST['neighbourhood_location']

    try:
        # Check if neighbourhood with passed in name and location exists
        neighbourhood = Neighbourhood.objects.filter(
            name=neigh_name, location=neigh_loc).first()

        return neighbourhood

    except:
        # Create new neighbourhood
        neighbourhood = Neighbourhood(
            name=neigh_name, location=neigh_loc, admin=request.user, occupants_count=1)

        neighbourhood.create_neighbourhood()
        return neighbourhood


@login_required
def setup_profile(request):

    if request.method == 'POST':

        try:
            # Get or create profile

            profile = Profile.objects.get(user=request.user)

            # If profile exists we update it
            profile.name = request.POST['full_names']
            profile.email = request.POST['email']
            profile.neighbourhood = get_or_create_neighbourhood(request)

            profile.save_profile()

        except:
            # Create new profile
            user = request.user
            name = request.POST['full_names']
            email = request.POST['email']
            neighbourhood = get_or_create_neighbourhood(request)
            # Update occupants count when creating new profile
            neighbourhood.update_occupants_count()

            profile = Profile(user=user, name=name, email=email,
                              neighbourhood=neighbourhood)
            profile.save_profile()

        finally:
            return render(request, 'setup_profile.html')

    return render(request, 'setup_profile.html')


@login_required
def setup_business(request):

    if request.method == 'POST':

        name = request.POST['business_name']
        email = request.POST['business_email']
        neighbourhood = get_or_create_neighbourhood(request)

        business = Business(name=name, email=email,
                            neighbourhood=neighbourhood, user=request.user)
        business.create_business()

        return render(request, 'setup_business.html')

    return render(request, 'setup_business.html')



def biz_list(reauest):
    businesses = Business.objects.all()
    return render(reauest, 'biz_list.html', {'businesses': businesses})