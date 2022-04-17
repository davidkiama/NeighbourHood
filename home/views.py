
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Profile, Neighbourhood

# Create your views here.

# Helper function to create profile


def home(request):
    return render(request, 'index.html')


def check_neighbourhood_obj(neigh_name, neigh_loc):

    try:
        # Check if neighbourhood with passed in name and location exists
        nei_obj = Neighbourhood.objects.filter(
            name=neigh_name, location=neigh_loc).first()

        if nei_obj:
            return nei_obj
        else:
            return False
    except:
        return False


@login_required
def setup_profile(request):

    if request.method == 'POST':
        user = request.user
        name = request.POST['full_names']
        email = request.POST['email']
        neigh_name = request.POST['neighbourhood_name']
        neigh_loc = request.POST['neighbourhood_location']

        neighbourhood = check_neighbourhood_obj(neigh_name, neigh_loc)
        if neighbourhood:
            neighbourhood.update_occupants_count()
        else:
            # Create new neighbourhood
            neighbourhood = Neighbourhood(
                name=neigh_name, location=neigh_loc, admin=request.user, occupants_count=1)

            neighbourhood.create_neighbourhood()

        # Create profile
        profile = Profile(user=user, name=name, email=email,
                          neighbourhood=neighbourhood)
        profile.save_profile()

    return render(request, 'setup_profile.html')
