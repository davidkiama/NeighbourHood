
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Profile, Neighbourhood, Business, Post

from django.contrib import messages

# Create your views here.

# Helper function to create profile


def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def contact(request):
    return render(request, 'contact.html')


def get_or_create_neighbourhood(request):

    neigh_name = request.POST['neighbourhood_name']
    neigh_loc = request.POST['neighbourhood_location']

    try:
        # Check if neighbourhood with passed in name and location exists
        neighbourhood = Neighbourhood.objects.filter(
            name=neigh_name, location=neigh_loc).first()

        if neighbourhood:
            return neighbourhood
        else:
            # Create new neighbourhood
            print('Creating new neighbourhood')
            neighbourhood = Neighbourhood(
                name=neigh_name, location=neigh_loc, admin=request.user, occupants_count=1)

            neighbourhood.create_neighbourhood()

            return neighbourhood

    except Exception as e:
        print(e)

        return None


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
            return redirect(home)

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

            return render(request, 'setup_profile.html')

    return render(request, 'setup_profile.html')


@login_required
def setup_business(request):

    if request.method == 'POST':

        name = request.POST['business_name']
        email = request.POST['business_email']
        neighbourhood = get_or_create_neighbourhood(request)
        neighbourhood.update_occupants_count()

        business = Business(name=name, email=email,
                            neighbourhood=neighbourhood, user=request.user)
        business.create_business()

        return redirect(home)

    return render(request, 'setup_business.html')


def biz_list(reauest):
    businesses = Business.objects.all()
    return render(reauest, 'biz_list.html', {'businesses': businesses})


def search_business(request):
    if 'business' in request.GET and request.GET['business']:
        search_term = request.GET.get('business')
        businesses = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {'message': message, 'businesses': businesses})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message, 'businesses': False})


def create_post(request):

    if request.method == 'POST':
        try:
            profile = Profile.objects.get(user=request.user)
        except Exception as e:
            print(e)
            messages.success(request, 'Must setup a profile.')

            # redirect to setup pofile
            return redirect(setup_profile)

        post_title = request.POST['post_title']
        post_content = request.POST['post_content']
        post_neighbourhood = profile.neighbourhood
        user = request.user

        post = Post(title=post_title, content=post_content,
                    neighbourhood=post_neighbourhood, user=user)
        post.create_post()

        return render(request, 'create_post.html')
    return render(request, 'create_post.html')
